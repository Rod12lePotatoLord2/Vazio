# RELATÓRIO – Controle de Configuração com Git

## 🗂️ Histórico de Commits

- **[Rod12lePotatoLord2]** - Adiciona função `somar`  
- **[Rod12lePotatoLord2]** - Adiciona função `multiplicar`  
- **[Juliana Andrade]** - Adiciona função `subtrair`  
- **[Juliana Andrade]** - Adiciona função `dividir` com verificação de divisão por zero  
- **[Juliana Andrade]** - Adiciona função `exponencial` (potência)

---

## 🏷️ Tags de Versão

- `v1.0`: Versão inicial com as quatro funções básicas: `somar`, `multiplicar`, `subtrair`, `dividir`
- `v1.1`: Versão com adição da função `exponencial`

---

## 🔍 Diferenças entre Versões (`git diff v1.0 v1.1`)

```diff
+def exponencial (a, b):
+    return a ** b

^41b0dfd (Rod12lePotatoLord2 2025-09-08 10:50:12 -0300  1) def somar(a, b):
c276cf41 (Rod12lePotatoLord2 2025-09-08 11:06:35 -0300  2)     return a + b
c276cf41 (Rod12lePotatoLord2 2025-09-08 11:06:35 -0300  4) def multiplicar(a, b):
c276cf41 (Rod12lePotatoLord2 2025-09-08 11:06:35 -0300  5)     return a * b
ab50386e (Juliana Andrade    2025-09-08 11:21:29 -0300  7) def subtrair (a, b):
0db59fb3 (Juliana Andrade    2025-09-08 11:35:23 -0300  8)     return a - b
0db59fb3 (Juliana Andrade    2025-09-08 11:35:23 -0300 10) def dividir(a, b):
0db59fb3 (Juliana Andrade    2025-09-08 11:35:23 -0300 11)     if b == 0:
0db59fb3 (Juliana Andrade    2025-09-08 11:35:23 -0300 12)         return "Erro: Divisão por 0!"
c8bcb27e (Juliana Andrade    2025-09-08 11:39:46 -0300 13)     return a / b
c8bcb27e (Juliana Andrade    2025-09-08 11:39:46 -0300 15) def exponencial (a, b):
c8bcb27e (Juliana Andrade    2025-09-08 11:39:46 -0300 16)     return a ** b

## Versão v1.2

### Alterações:
- Implementação de chamadas diretas das funções matemáticas
- Menu interativo para o usuário via terminal
- Tratamento de erro para divisão por zero
- Refatoração de código para maior legibilidade

### Responsabilidades

### Rod12lePotatoLord2 (Rodrigo) foi responsável pelas funções: somar, multiplicar, melhorias no código, interface interativa tag v1.1 e v1.2
### Juliana Andrade foi responsável pelas funções: subtrair, dividir, exponencial, tag v1.0