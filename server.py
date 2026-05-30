import http.server
import urllib.parse
import os

TEMPLATES_DIR = 'templates'

class ContactsHandler(http.server.BaseHTTPRequestHandler):
    """Обработчик HTTP-запросов"""

    def do_GET(self):
        """Любой GET-запрос возвращает страницу контактов"""
        self._send_html_response('contacts.html')

    def do_POST(self):
        """Обработка POST-запроса от формы"""
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_data = urllib.parse.parse_qs(post_data)

        form_data = {key: value[0] for key, value in parsed_data.items()}
        print("Получены данные от пользователя:")
        print(f"Имя: {form_data.get('name')}")
        print(f"Почта: {form_data.get('email')}")
        print(f"Сообщение: {form_data.get('message')}")
        print("-" * 40)

        self._send_html_response('contacts.html')

    def _send_html_response(self, filename, status_code=200):
        """Отправляет HTML-файл с заданным статусом, используя контекстный менеджер"""
        filepath = os.path.join(TEMPLATES_DIR, filename)
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
            self.send_response(status_code)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self._send_error_page(500)
        except Exception:
            self._send_error_page(500)

    def _send_error_page(self, code):
        """Отправляет страницу ошибки (404 или 500)"""
        if code == 404:
            page = '404.html'
        else:
            page = '500.html'
        filepath = os.path.join(TEMPLATES_DIR, page)
        try:
            with open(filepath, 'rb') as f:
                content = f.read()
            self.send_response(code)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content)
        except Exception:
            self.send_response(code)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(f"Error {code}".encode())

def run_server(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, ContactsHandler)
    print(f"Сервер запущен на http://localhost:{port}")
    print("Любой GET-запрос возвращает страницу контактов.")
    print("POST-запросы от формы будут выводить данные в консоль.\n")
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
