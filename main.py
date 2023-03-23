from app import server

# Se corre la aplicación
if __name__ == "__main__":
	server.run(host="0.0.0.0", port=8050, debug=True, use_reloader=True)