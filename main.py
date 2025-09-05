# -*- coding: utf-8 -*-

"""
Projeto: Conversor de Markdown para HTML
Descrição: Uma ferramenta CLI que lê um arquivo Markdown (.md) e o converte para um arquivo HTML (.html).
             O nome do arquivo de saída é opcional; se não for fornecido, será o mesmo do arquivo de entrada com a extensão .html.

Como usar:
  python main.py <arquivo_entrada.md> [arquivo_saida.html]

Exemplos:
  python main.py exemplo.md
  python main.py exemplo.md output/exemplo.html

Dependências:
  pip install markdown2
"""

import sys
import os
import argparse

try:
    import markdown2
except ImportError:
    print("Erro: biblioteca 'markdown2' não está instalada. Instale com: pip install markdown2")
    sys.exit(1)


def converter_md_para_html(entrada, saida):
    try:
        with open(entrada, 'r', encoding='utf-8') as f:
            conteudo_md = f.read()
    except FileNotFoundError:
        print(f"Arquivo de entrada não encontrado: {entrada}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo {entrada}: {e}")
        sys.exit(1)

    html = markdown2.markdown(conteudo_md, extras=["fenced-code-blocks", "tables"])

    diretorio_saida = os.path.dirname(saida)
    if diretorio_saida and not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    try:
        with open(saida, 'w', encoding='utf-8') as f:
            f.write(html)
    except Exception as e:
        print(f"Erro ao salvar o arquivo {saida}: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Converte arquivo Markdown (.md) para HTML.")
    parser.add_argument('entrada', help='Arquivo Markdown de entrada (.md)')
    parser.add_argument('saida', nargs='?', help='Arquivo HTML de saída (.html) opcional')
    args = parser.parse_args()

    entrada = args.entrada
    if not entrada.lower().endswith('.md'):
        print('Aviso: extensão de arquivo de entrada não é .md')

    saida = args.saida
    if not saida:
        base = os.path.splitext(entrada)[0]
        saida = base + '.html'

    converter_md_para_html(entrada, saida)
    print(f'Arquivo convertido com sucesso!')
    print(f'Entrada: {entrada}')
    print(f'Saída: {saida}')


if __name__ == '__main__':
    main()
