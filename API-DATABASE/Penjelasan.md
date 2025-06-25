# 📡 Flask + InfluxDB API untuk Data Sensor IoT (DHT11)

Script ini adalah sebuah API sederhana berbasis **Flask** yang digunakan untuk menerima data sensor (suhu dan kelembaban) dan menyimpannya ke dalam **InfluxDB** menggunakan protokol HTTP POST.

---

## 🔧 Teknologi yang Digunakan

- **Flask** – Web framework Python
- **InfluxDB Client Python** – Library resmi untuk menulis ke InfluxDB v2
- **InfluxDB v2.x** – Time-series database untuk data sensor IoT

---

## 📥 Endpoint API

### `POST /sensor`

- **Deskripsi**: Menerima data dari sensor (suhu dan kelembaban)
- **Header**: 
- **Contoh Payload**:
  ```json
  {
    "temperature": 27.5,
    "humidity": 65.2
  }
  ```

- **Response**:
  ```
  ok
  ```

---

## 🗃️ Struktur Data InfluxDB

- **Measurement**: `iotDHT11_data`
- **Bucket**: `DHT11`
- **Organization**: `test1`
- **Fields**:
- `temperature` (float)
- `humidity` (float)

---

## 🛠️ Konfigurasi Koneksi (di dalam script)

```python
client = InfluxDBClient(
  url="http://10.0.1.148:8086/",
  token="YOUR_TOKEN",
  org="test1"
)
