#! /usr/bin/env python3


import os
import requests

file_dir = "~/supplier-data/descriptions"
file_path = os.path.expanduser(file_dir)
files = os.listdir(file_path)
dict_desc = {}
server_domain = "http://12.34.567.890"


def read_file():
    for file_name in files:
        with open(file_path + '/' + file_name, "r") as file:
            dict_desc["name"] = file.readline().rstrip()
            dict_desc["weight"] = int(file.readline().split(" ")[0])
            dict_desc["description"] = file.readline().rstrip()
            dict_desc["image_name"] = file_name[:-4] + ".jpeg"

        post_dict(dict_desc)


def post_dict(dict_data):
    response = requests.post(server_domain + "/" + "fruits" + "/", json=dict_data)
    if response.status_code == 201:
        print("posted : ", dict_data["name"])


if __name__ == "__main__":
    read_file()
