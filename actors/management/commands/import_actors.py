from django.core.management.base import BaseCommand  # importação padrão
import csv  # biblioteca para ler csv
from datetime import datetime  # tratar datas
from actors.models import Actor  # importando o bd


# para rodar basta ir no terminal e rodar python manage.py import_actors actors.csv


class Command(BaseCommand):  # sempre assim
    def add_arguments(self, parser):
        parser.add_argument(
            "file_name",
            type=str,
            help="Nome do arquivo CSV com atores",
        )

    def handle(self, *args, **options):  # sempre assim
        file_name = options["file_name"]  # passando qual arquivo

        with open(file_name, "r", encoding="utf-8") as file:  # abre o arquivo
            reader = csv.DictReader(file)  # le o arquivo
            for row in reader:  # percorre linha a linha
                name = row["name"]  # coluna name
                birthday = datetime.strptime(  # tratando a coluna de aniversario
                    row["birthday"], "%Y-%m-%d"
                ).date()
                nationality = row["nationality"]  # coluna nacionalidade
                # a cada vez que rodar ele printa o nome do ator que foi importado naquele loop
                self.stdout.write(self.style.NOTICE(name))

                Actor.objects.create(  # adicionando no bd os dados coletados do csv
                    name=name,
                    birthday=birthday,
                    nationality=nationality,
                )
        # se a importação deu certo ele printa essa mensagem
        self.stdout.write(self.style.SUCCESS("ATORES IMPORTADOS COM SUCESSSO!"))
