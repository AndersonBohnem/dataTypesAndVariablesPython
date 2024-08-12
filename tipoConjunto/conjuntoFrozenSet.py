import os

def clearConsole():
    os.system('cls')

#Conjunto FrozenSet

clearConsole()

permissionAdmin = frozenset(['criar', 'editar', 'deletar', 'visualizar'])
permissionUser = frozenset(['visualizar', 'comentar'])
permissionGuest = frozenset(['visualizar'])


descriptionRoles = {
    permissionAdmin: "Administrador - acesso total",
    permissionUser: "Usuário - acesso limitado",
    permissionGuest: "Convidado - acesso de visualização"
}

print("Conjunto FrozenSet utilizado para criar direcionarios que não podem ser mudados")
print("Mais utilizado para declarar permissão de usuários\n")
print("Exemplos de Acesso:\n\n" , descriptionRoles[permissionAdmin] , "\n" , permissionAdmin , 
      "\n\n" , descriptionRoles[permissionUser] , "\n" , permissionUser , 
      "\n\n" , descriptionRoles[permissionGuest] , "\n" , permissionGuest ,)
