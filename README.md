# sistema_bancario_em_python

Este é um pequeno sistema bancario em python com operacoes de saque, deposito e visualização.

##### Esta é a versão de um script sem interface gráfica que simula operações bancárias de saque, deposito e extrato na conta de um usuário fictício.

`userInput`: Função principal cujo objetivo é executar toda a regra de negócio da aplicação (Retorno nulo)

`selectASpecificOperation`: Uma factory que retorna em um objeto uma das operações bancárias possíveis sacar, depositar e visualizar o extrato. (Retorna um objeto)

`accountWithDraw`: Operação retornada pelo `selectASpecificOperation`, responsável por realizar operação de saque. (Retorna um objeto)

`accountDeposit`: Operação retornada pelo `selectASpecificOperation`, responsável por realizar operação de depósito. (Retorna um objeto)

`accountView`: Operação retornada pelo `selectASpecificOperation`, responsável por realizar operação de visualização de extrato. (Retorna um objeto)

#### Variáveis e Constantes

| Nome                                  | descrição                           |
| ------------------------------------- | ----------------------------------- |
| currentAccount["depositStatement"]    | registro de depósitos realizados    |
| currentAccount["withdrawalStatement"] | registro de saques realizados       |
| currentAccount["totalBalance"]        | valor total da conta do usuário     |
| LIMIT_OF_DAILY_WITHDRAWALS            | limite de saques diários permitidos |
| LIMIT_PRICE_PER_WITHDRAWAL            | quantia limite diária para sacar    |
