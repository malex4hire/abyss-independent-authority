FROM eclipse-temurin:21-jdk-jammy

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN python3 -m venv /opt/authority-venv \
    && /opt/authority-venv/bin/pip install --no-cache-dir -r requirements.txt

COPY java java
COPY adapters adapters
COPY run_demo.py .
RUN mkdir -p .demo-build audit \
    && javac --release 21 -d .demo-build $(find java -name '*.java') \
    && /opt/authority-venv/bin/python run_demo.py > /tmp/demo-output \
    && grep -q "3 blocked bypass attempts" /tmp/demo-output

CMD ["/opt/authority-venv/bin/python", "run_demo.py"]
