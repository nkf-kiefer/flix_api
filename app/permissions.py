from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Obtém o codename da permissão correspondente ao método HTTP atual(delete,patch,put etc...).
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        # Se não foi possível determinar um codename, nega acesso.
        if not model_permission_codename:
            return False

        # Verifica se o usuário autenticado possui a permissão para aquele metodo.
        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(
        self, method, view
    ):  # feito após verificação de permissão
        try:
            model = view.queryset.model

            # Informações do modelo
            model_name = model._meta.model_name  # model da app
            app_label = model._meta.app_label  # app

            # Converte o método HTTP em sufixo de ação (add, view, change, delete).
            action = self.__get_action_sufix(method)

            # Retorna a string completa usada pelo Django para codenames de permissão.
            return f"{app_label}.{action}_{model_name}"

        except AttributeError:
            # Se não houver queryset ou a model não puder ser obtida, nega acesso.
            return None

    def __get_action_sufix(
        self, method
    ):  # traduzindo os metodos e atrbuindo a eles um nome para compor a get_model_permission_codename
        method_actions = {
            "GET": "view",  # Leitura de recursos (lista ou detalhe)
            "POST": "add",  # Criação de novos recursos
            "PUT": "change",  # Substituição total de recursos
            "PATCH": "change",  # Atualização parcial
            "DELETE": "delete",  # Exclusão
            "OPTIONS": "view",  # Metadados sobre a rota
            "HEAD": "view",  # Similar ao GET, sem corpo
        }
        # Caso o método não esteja no dicionário, retorna string vazia (nega permissão).
        return method_actions.get(method, "")
