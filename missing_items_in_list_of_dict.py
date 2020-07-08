# This is to determine the missing list item in a list of dicts.

tenant_list_of_region = ["90", "91", "92"]
missing_accounts = []
stack_instances = [
    {
        "Account": "90",
        "Status": "CURRENT"

    },
    {
        "Account": "91",
        "Status": "CURRNT"

    }
]

for tenant_id in tenant_list_of_region:
    check_exists = [stack.get('Account') == tenant_id and stack.get('Status') == 'CURRENT' for stack in stack_instances]
    print(check_exists, "val") #Boolean value list ex: ([True, False], 'val')
    if not any(check_exists): #any() function returns True if any element of an iterable is True.
        missing_accounts.append(tenant_id)
        print(missing_accounts)

print(missing_accounts)