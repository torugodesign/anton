"""Servidor local sem cache — evita servir HTML/CSS/JS desatualizados
durante o desenvolvimento (python -m http.server não envia Cache-Control,
então o navegador às vezes reaproveita versões antigas dos arquivos)."""
import http.server
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        super().end_headers()


http.server.test(HandlerClass=NoCacheHandler, port=PORT)
