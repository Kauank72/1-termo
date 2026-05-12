# Notas de Aula: Sistemas Operacionais
**Tópicos:** Linux, CLI Windows, Virtualização e Segurança Cibernética

---

## 1. Máquinas Virtuais (Virtualização)
A virtualização permite executar vários sistemas operacionais em um único hardware físico através de um **Hypervisor**.

*   **Vantagens:** Isolamento de ambientes, testes de softwares inseguros e economia de hardware.
*   **Softwares Comuns:** VirtualBox, VMware e Hyper-V.
*   **Conceito Chave:** O sistema operacional real é o **Host** (Hospedeiro) e o virtualizado é o **Guest** (Convidado).

---

## 2. Distribuições Linux
O Linux é um **Kernel**. Uma "Distro" é o Kernel somado a ferramentas, interfaces e gerenciadores de pacotes.

### Principais Famílias:
*   **Debian/Ubuntu:** Focadas em estabilidade e facilidade de uso (usam `.deb` e `apt`).
*   **Red Hat/Fedora/CentOS:** Comuns em ambientes corporativos e servidores (usam `.rpm` e `dnf/yum`).
*   **Arch Linux:** Focada em usuários avançados e personalização total.
*   **Kali Linux:** Especializada em testes de penetração e segurança.

---

## 3. Operação do Windows via CLI (Terminal)
O uso da linha de comando no Windows (CMD ou PowerShell) é essencial para administração de sistemas.

### Comandos Essenciais (CMD):
*   `dir`: Lista arquivos e pastas.
*   `cd`: Navega entre diretórios.
*   `ipconfig`: Exibe configurações de rede e endereço IP.
*   `tasklist` / `taskkill`: Gerencia processos em execução.
*   `systeminfo`: Exibe detalhes do hardware e do SO.

---

## 4. Segurança Cibernética no SO
A segurança do sistema operacional é a primeira linha de defesa contra ataques.

### Pilares de Proteção:
1.  **Gerenciamento de Usuários:** Princípio do Privilégio Mínimo (não usar conta Admin para tarefas diárias).
2.  **Atualizações (Patch Management):** Correção de vulnerabilidades conhecidas.
3.  **Firewall:** Controle de tráfego de entrada e saída.
4.  **Log de Eventos:** Monitoramento de atividades suspeitas no sistema.

---

## Laboratório Prático
1.  **Configuração:** Criar uma VM com Ubuntu Linux no VirtualBox.
2.  **CLI:** Utilizar o CMD do Windows para identificar o IP da máquina real.
3.  **Segurança:** Configurar uma regra simples de firewall para bloquear um serviço específico.

---

## Links e Referências
*   [Guia de Comandos Linux](https://linux.org)
*   [Documentação Microsoft CLI](https://microsoft.com)
*   [Certificação CompTIA Security+](https://comptia.org)
