# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        alll = {}
        
        for domain in cpdomains:
            freq, full_domain = domain.split(" ")
            freq = int(freq)
            parts = full_domain.split(".")
            

            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                if subdomain in alll:
                    alll[subdomain] += freq
                else:
                    alll[subdomain] = freq
        
   
        return [f"{value} {key}" for key, value in alll.items()]
