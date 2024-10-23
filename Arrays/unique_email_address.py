from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        address = set()

        for s in emails:
            local, domain = s.split("@")
            local = local.replace(".","")
            local = local.split("+")[0]
            
            address.add(local + "@" + domain)

        return len(address)