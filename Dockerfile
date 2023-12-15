FROM python:3

RUN apt update && DEBIAN_FRONTEND=noninteractive apt install -y python3-pip
RUN pip3 install pandas matplotlib upsetplot numpy scikit-learn