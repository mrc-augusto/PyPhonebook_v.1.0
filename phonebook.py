import os

def add_contact(phonebook):
  contact_name = input('Digite o nome do contato: ')
  contact_phone = input('Digite o número de telefone do contato: ')
  contact_email = input('Digite o email do contato: ')

  contact={
    'name': contact_name,
    'phone': contact_phone,
    'email': contact_email,
    'favorite': False
  }
  phonebook.append(contact)

  print(f'Contato {contact_name} adicionado com sucesso!')
  return

phonebook = []

while True:
  print('\nMenu da Agenda Telefônica')
  print('1. Adicionar contato')
  print('2. Visualizar lista de contatos:')
  print('3. Editar um contato')
  print('4. Marcar/Desmarcar contato como favorito')
  print('5. Visualizar contatos favoritos')
  print('6. Deletar contato')
  print('7. Sair da Agenda Telefônica')

  choice = input('Escolha a opção desejada (1-7): ')

  if choice == '1':
    add_contact(phonebook)
    os.system('cls' if os.name == 'nt' else 'clear')

  elif choice == '2':
    os.system('cls' if os.name == 'nt' else 'clear')

    pass

  elif choice == '3':
    os.system('cls' if os.name == 'nt' else 'clear')

    pass

  elif choice == '4':
    os.system('cls' if os.name == 'nt' else 'clear')

    pass

  elif choice == '5':
    os.system('cls' if os.name == 'nt' else 'clear')

    pass

  elif choice == '6':
    os.system('cls' if os.name == 'nt' else 'clear')

    pass

  elif choice == '7':
    break

  else:
    print('Opção inválida. Por favor, escolha uma opção entre 1 e 7.')

print('Obrigado por usar a Agenda Telefônica. Até logo!')
