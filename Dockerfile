# --- Base image ---
FROM python:3.10-bullseye

# --- Set working directory ---
WORKDIR /app

# --- Copy dependency list first for caching ---
COPY requirements.txt .

# --- Install dependencies ---
RUN pip install --no-cache-dir -r requirements.txt

# --- Copy the rest of the application ---
COPY . .

# --- Default command ---
CMD ["python3", "bot.py"]


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
