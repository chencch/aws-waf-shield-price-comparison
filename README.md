# aws-waf-shield-price-comparison

As [AWS Shield Pricing](https://aws.amazon.com/shield/pricing/) mentioned:

> Shield Advanced subscription includes certain AWS WAF usage for Shield protected resources at no additional cost. This includes the monthly fees for Web ACL and Rules as well as request fees for Web ACLs **with default limits**. All other WAF features such as Intelligent Threat Mitigation (e.g., Bot and Fraud Control) or request fees for Web ACLs with WCUs greater than the default will still incur WAF charges. See [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/) for more details.

Some customers may consider subscribing Shield Advanced to reduce their WAF cost. This python script can be used for cost estimation, comparing WAF-only cost and Shield Advanced cost.

## How to use it

1. Install Python3 packages with pip and `requirements.txt`.
```python
$ pip install -r requirements.txt
```

2. Customize the values of the following variables.
- `aos` - Average Object Size in KB
  - AOS = Actual value of monthly DTO / Actual value of the total number of requests per month
  - The requests include all HTTP request methods (GET, POST, etc.), HTTP and HTTPS protocols, as well as blocked requests.
- `webacl_num` - The number of WAF Web ACLs
- `rule_num` - The total number of WAF rules (not rule groups)

3. Execute the Python script with Python3
```python
$ python main.py
```

## For Private Price scenario

If users have a private price contract, just change the values of the following variables:
- `req_price` - WAF request price per 1 million requests (for inspection up to 1500 WCUs and default body size)
- `subsc` - Price of Shield monthly subscription
- `tier1` - Shield DTO price per GB for first 100 TB
- `tier2` - Shield DTO price per GB for next 400 TB
- `tier3` - Shield DTO price per GB for next 500 TB
- `tier4` - Shield DTO price per GB for above 1,000 TB

## Notes

According to [AWS Shield Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/request-refund.html): 
> If you're subscribed to AWS Shield Advanced and you experience a DDoS attack that increases utilization of a Shield Advanced protected resource, you can request a credit for charges related to the increased utilization to the extent that it is not mitigated by Shield Advanced. Credits are available only for the following types of charges: Amazon CloudFront HTTP/HTTPS requests, CloudFront data transfer out, Amazon Route 53 queries, AWS Global Accelerator standard accelerator data transfer, load balancer capacity units for Application Load Balancer, and usage spikes on protected Amazon Elastic Compute Cloud (Amazon EC2) instances.

So even though Shield Advanced is more expensive than WAF-only in some conditions, it is still valuable, especially considering its [security benefits](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html).