FROM python:3.8.0


COPY ./ /mslesion_seg
WORKDIR /mslesion_seg

RUN pip3 install --upgrade pip
RUN pip3 uninstall -y setuptools
RUN pip3 install  --no-cache-dir setuptools
RUN pip3 install  --no-cache-dir -r requirements.txt

CMD ["python", "segment_lesion.py"]