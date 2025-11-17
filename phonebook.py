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

def show_contacts_list(phonebook):
  if not phonebook:
    print('A lista de contatos está vázia.')
    return
  
  print('Lista de Contatos:')
  for index, contact in enumerate(phonebook):
    fav_status = '⭐' if contact['favorite'] else 'Não'
    print(f'{index +1}. \nNome: {contact['name']} \nTelefone: {contact['phone']}  \nEmail: {contact['email']} \nFavorito: {fav_status}')

def edit_contact(phonebook):
  if not phonebook:
    print('A lista de contatos está vázia. Adicione um contato antes de editar.')
    input ('Pressione Enter para continuar...')
    os.system('cls' if os.name == 'nt' else 'clear')
    return

  show_contacts_list(phonebook)
  
  index = int(input('Digite o número do contato que deseja editar: ')) - 1

  if 0 <= index < len(phonebook):
    phonebook[index]['name'] = input('Digite o novo nome do contato: ')
    phonebook[index]['phone'] = input('Digite o novo número de telefone: ')
    phonebook[index]['email'] = input('Digite o novo email do contato: ')
    print('Contato atualizado com suceso!')
  else:
    print('Contato não encontrado ou não existe na agenda')
    input ('Pressione Enter para continuar...')
  


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
    show_contacts_list(phonebook)
    # os.system('cls' if os.name == 'nt' else 'clear')


  elif choice == '3':
    edit_contact(phonebook)
    os.system('cls' if os.name == 'nt' else 'clear')

    

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
