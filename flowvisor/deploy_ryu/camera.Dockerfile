FROM python:3.8-slim

# Install dependency
RUN pip install ryu==4.34 eventlet==0.30.2 requests==2.28.2 urllib3==1.26.15

# Set working directory
WORKDIR /ryu_app

# Copy Ryu App ke container
COPY ryucamera.py /ryu_app/

# Expose OpenFlow port
EXPOSE 6635

# Jalankan Ryu app
CMD ["ryu-manager", "ryucamera.py"]
