#!/root/nsd1905/bin/python
# import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
# from ansible.plugins.callback import CallbackBase
import ansible.constants as C

def ansible_adhoc(vault_pass=None,hosts_file_source=None,hosts=None,module=None,args=None):
    #配置ansible 执行过程中所用到的参数
    #connection 是链接类型， 有三种选项 ： 1.local 表示本地执行 ，2.ssh 表示通过ssh连接后执行 ，3. smart自动选择（default)
    Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
    options = Options(connection='smart', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

    # initialize needed objects
    #ansible会用到各种各样的文件， 如 json, yaml, ini等， 这些文件的内容需要转成python的数据类型，DataLoader自动进行转换
    loader = DataLoader() # Takes care of finding and reading yaml, json and ini files
    #各种密码 ,如果有利用ansible-vault 加密，尝试使用vault_pass 所指定的密码来解密
    passwords = dict(vault_pass=vault_pass)

    # Instantiate our ResultCallback for handling results as they come in. Ansible expects this to be one of its main display outlets
    # results_callback = ResultCallback()

    # create inventory, use path to host config file as source or hosts in a comma separated string
    #inventory = InventoryManager(loader=loader, sources='localhost,')
    inventory = InventoryManager(loader=loader, sources= hosts_file_source)

    # variable manager takes care of merging all the different sources to give you a unifed view of variables available in each context
    #变量管理器
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # create datastructure that represents our play, including tasks, this is basically what our YAML loader does internally.


    play_source =  dict(
            name = "Ansible Play",
            hosts = hosts,
            gather_facts = 'no',
            tasks = [
                dict(action=dict(module=module, args=args), register='shell_out'),
                dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
             ]
        )   #gather_facts 是否使用setup 模块收集主机信息

    # Create play object, playbook objects use .load instead of init or new methods,
    # this will also automatically create the task objects from the info provided in play_source
    #创建play实例
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # Run it - instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
    #创建任务队列管理器实例
    tqm = None
    try:
        tqm = TaskQueueManager(
                  inventory=inventory,
                  variable_manager=variable_manager,
                  loader=loader,
                  options=options,
                  passwords=passwords,
                  # stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin, which prints to stdout

              )
        result = tqm.run(play) # most interesting data for a play is actually sent to the callback's methods
    finally:
        # we always need to cleanup child procs and the structres we use to communicate with them
        if tqm is not None:
            tqm.cleanup()

        # Remove ansible tmpdir
        shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


if __name__ == '__main__':
    ansible_adhoc(hosts_file_source='/root/myansible/hosts',hosts='dbservers', module='shell',args='id root')