import numpy as np
import matplotlib.pyplot as plt

# Average object size (KB)
# AOS = Actual value of monthly DTO / Actual value of the total number of requests per month (GET+POST+Others)
aos = 1

webacl_num = 1
rule_num = 10

# Monthly request number (Million)
req = np.arange(0, 10000, 1)

# WAF monthly fee (excluding Intelligent Threat Mitigation rules)
# Web ACL	$5.00 per month
# Rule	$1.00 per month
# $0.60 per 1 million requests (for inspection up to 1500 WCUs and default body size)
req_price = 0.6
waf = webacl_num * 5 + rule_num * 1 + req * req_price

# Monthly Shield DTO (GB)
# Please note that the contents of AWS and other companies are different even with the same GB notation!
# AWS：1 GB = 1GiB = 1024 x 1024 x 1024 bytes
# Competitor example: 1 GB = 1000 x 1000 x 1000 bytes
# Unit conversion is required for accurate estimates
# Example: 30 TB of third-party CDN = 30x1000x1000x1000x1000/1024/1024/1024 = 27.28 TiB
shield = aos * req * 1000 * 1000 / 1024 / 1024

# Shield monthly fee for CloudFront protection
# Monthly subscription $3,000
subsc = 3000

# First 100 TB	$0.025 per GB
tier1 = 0.025
# Next 400 TB	$0.02 per GB
tier2 = 0.02
# Next 500 TB	$0.015 per GB
tier3 = 0.015
# Next 4 PB	    $0.01 per GB
tier4 = 0.01

for i in np.nditer(shield, op_flags=['readwrite']):
    if i <= 100*1024:
        i[...] = subsc + tier1*i
    elif 100*1024 < i <= 500*1024:
        i[...] = subsc + tier1*100*1024 + tier2*(i-100*1024)
    elif 500*1024 < i <= 1000*1024:
        i[...] = subsc + tier1*100*1024 + tier2*400*1024 + tier3*(i-500*1024)
    else:
        i[...] = subsc + tier1*100*1024 + tier2*400*1024 + tier3*500*1024 + tier4*(i-1000*1024)

plt.plot(req, waf, 'r')        # Red line represents WAF cost
plt.plot(req, shield, 'b')     # Blue line represents Shield Adv cost
plt.title('WAF & Shield price comparison')
plt.xlabel('Requests (Million)')
plt.ylabel('Monthly cost $')
plt.show()