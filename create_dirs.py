import os


for d in range(1,9):
    os.makedirs(f"./data/data{d}-1")
    os.makedirs(f"./data/data{d}-2")


# for d in range(1,5):
#   txt =  f"""minio1-{d}:
#     image: minio/minio:RELEASE.2021-06-17T00-10-46Z
#     hostname: minio1-{d}
#     volumes:
#       - ./data1/data{d}-1:/data1
#       - ./data1/data{d}-2:/data2
#     expose:
#       - "9000"
#     environment:
#       MINIO_ROOT_USER: minio
#       MINIO_ROOT_PASSWORD: minio123
#       MINIO_ACCESS_KEY: V42FCGRVMK24JJ8DHUYG
#       MINIO_SECRET_KEY: bKhWxVF3kQoLY9kFmt91l+tDrEoZjqnWXzY9Eza
#     command: server http://minio1-{'{1...12}'}/data{'{1...2}'}
#     healthcheck:
#       test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
#       interval: 30s
#       timeout: 20s
#       retries: 3"""
#   print(txt)