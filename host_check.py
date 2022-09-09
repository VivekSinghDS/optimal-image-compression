import requests ## to use the POST method we use a library named requests
# url = 'http://0.0.0.0:5000/predict'
url= "http://ae0b3a91bc8b543558bbddc1e7947d31-594062275.us-east-1.elb.amazonaws.com:5000/predict" # eks deployment
# url = "http://optimalimage8-env.eba-umrpekgu.us-east-2.elasticbeanstalk.com/predict" # aws beanstalk deployment
url = "http://ec2-44-204-227-255.compute-1.amazonaws.com:80/predict"
# url = "http://127.0.0.1:8080/predict"
url_r = {
    "image_path":"https://images.contentstack.io/v3/assets/blt5ac836f818fcdeb2/blt588212a6b0619c3d/62d4ed04a80c6d36eaa140a7/sample20.jpg"
}

#https://images.contentstack.io/v3/assets/blt5ac836f818fcdeb2/bltfce3adbfadd3e64b/62c67b2a74e36137c193d1dc/8e2bc05c-2f87-4e83-8867-54dca98a6bd6.jpeg
response = requests.post(url, json=url_r) ## post the customer information in json format
result = response.json() ## get the server response
print(result)