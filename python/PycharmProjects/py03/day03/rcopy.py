#!/root/nsd1905/bin/python
import shutil

from ansible.module_utils.basic import AnsibleModule


def main():
    module=AnsibleModule(
        argument_spec=dict(
            source=dict(required=True,type='str'),
            dest=dict(required=True,type='str')
        )

    )
    shutil.copy(src=module.params['source'],dst=module.params['dest'])
    module.exit_json(changed=True)


if __name__ == '__main__':
    main()
