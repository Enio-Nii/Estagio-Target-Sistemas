# Função para inverter uma string
def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Loop para percorrer a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  # Adiciona o caractere à nova string
    
    return string_invertida

# Entrada da string (pode ser alterada para qualquer string desejada)
string_original = input("Digite uma string a ser invertida: ")

# Chama a função e exibe o resultado
string_resultado = inverter_string(string_original)
print(f"String invertida: {string_resultado}")
