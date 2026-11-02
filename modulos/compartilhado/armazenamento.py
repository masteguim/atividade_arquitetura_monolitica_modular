"""Persistência simples em TXT (uma linha JSON por registro)."""
import json
from pathlib import Path

PASTA = Path(__file__).resolve().parents[2] / "dados_txt"
PASTA.mkdir(parents=True, exist_ok=True)

def ler(nome):
    arquivo = PASTA / nome
    if not arquivo.exists():
        return []
    with arquivo.open(encoding="utf-8") as f:
        return [json.loads(linha) for linha in f if linha.strip()]

def salvar(nome, registros):
    arquivo = PASTA / nome
    temporario = arquivo.with_suffix('.tmp')
    with temporario.open("w", encoding="utf-8") as f:
        for registro in registros:
            f.write(json.dumps(registro, ensure_ascii=False) + "\n")
    temporario.replace(arquivo)
