import requests
import lxml
import os
from bs4 import BeautifulSoup
import smtplib
my_email = os.environ.get("EMAIL")
my_pass = os.environ.get("PASS")
header_info = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'Accept-Language': "en-US,en;q=0.9",
}
product_html = requests.get("https://www.amazon.in/Park-Avenue-Luxury-Grooming-Collection/dp/B00G23S4YS/ref"
                            "=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=XPb2R&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7"
                            "-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969"
                            "-4220-8ac7-6dc7c0447352&pf_rd_r=45QHXP53ZZAEBXP9XRRP&pd_rd_wg=Mv8aG&pd_rd_r=078c722c"
                            "-fe1f-4048-be0b-159da475804f&pd_rd_i=B00G23S4YS", headers=header_info)
# print(product_html.text)
print(product_html.url)
product_soup = BeautifulSoup(product_html.text, features='lxml')
# print(product_soup.get_text())

product_price = product_soup.select_one(selector="#corePriceDisplay_desktop_feature_div .a-price-whole")
final_price = int(product_price.get_text())

if final_price < 600:
    connect = smtplib.SMTP_SSL("smtp.gmail.com", port=465)
    connect.login(user=my_email, password=my_pass)
    connect.sendmail(from_addr=my_email, to_addrs=my_email,
                     msg=f"Subject: Your desired product is at lowest price!\n"
                         f"\nHurry up & head to : {product_html.url} to buy before the price hits the roof\n")
    connect.close()
