#!/root/nsd1905/bin/python
import wget

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec=dict(
            url=dict(required=True, type='str'),
            dest=dict(required=True, type='str')
        )

    )
    wget.download(url=module.params['url'],out=module.params['dest'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
