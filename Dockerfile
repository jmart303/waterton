FROM ubuntu:22.04
WORKDIR /opt/test/build
RUN apt-get update && apt-get install -y python3 python3-pip && pip install boto3==1.28.20 requests==2.28.2
ENV PYTHONPATH="${PYTHONPATH}:/opt/test/build/"
COPY /aws_inventory /opt/test/build/aws_inventory/
COPY /aws_inventory/scripts/get_ec2_instances.py /opt/test/build/scripts/