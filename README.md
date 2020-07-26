
# Filesync
    
O sistema oferece uma solução para sincronia de arquivos digitais entre estações de trabalho ou servidores dentro de uma rede. Esta sincronia será realizada automaticamente através de tarefas de sincronia previamente configuradas pelo operador da ferramenta.

Esta ferramenta foi desenvolvida e documentada como artigo final no curso de Redes de Computadores na Faculdade SENAC Porto Alegre. Para consulta do artigo em sua versão publicada no formato SCB, favor utilizar o link abaixo:

[Artigo Filesync](https://github.com/lbmello/file-sync/blob/master/Artigo%20FileSync.pdf)

## Introdução

Em redes de grande porte, aonde existe um fluxo massivo de dados em trânsito, pode ser um desafio manter quaisquer informações sincronizadas entre os diversos membros desta rede. Grandes distâncias geográficas, diferentes configurações entre os equipamentos e diferentes características entre os links de comunicação podem gerar grandes atrasos ou falhas no envio destes dados.
    
Com o crescimento da internet na última década e com a transformação digital que diversas empresas vem passando, notou-se um grande aumento na quantidade de dados gerados e trocados entre redes. Juntamente deste aumento de demanda surge um problema, como manter estes dados sempre seguros, disponíveis e sincronizados dentro de uma rede massiva? E como manter essa necessidade crescente por tŕafego de dados? 
    
A maioria das empresas baseadas na estrutura de matriz/filial gera um grande volume de dados e de tráfego de redes entre todas suas localidades. Seja este tráfego gerado pelos funcionários acessando os sistemas internos da empresa, realizando envio de e-mails e mensagens de texto, imagens ou documentos corporativos em geral.
    
Para que os arquivos gerados sempre estejam íntegros e disponíveis é imprescindível que existam sistemas confiáveis de gerência de arquivos, sincronias de dados e redundâncias de informações, para que nenhum dado seja perdido, em nenhuma circunstância. Levando em conta estes dois requisitos, desenvolveu-se o File-Sync.
    
Essa ferramenta permite a troca de dados entre computadores de uma rede, utilizando-se de tarefas de sincronia configuradas pelo operador de forma simplificada. Tarefas estas, facilitam a gerência sobre os dados sincronizados, a periodicidade de suas sincronias e se existiram alterações de conteúdo nos arquivos.
    
O projeto foi desenvolvido utilizando a linguagem de programação Python, mais especificamente em sua versão 3.8, executada em sistema Linux. O projeto subdivide-se nos módulos de dados, entrada, saída, interno, api, cli e sincronia.


## Instalação da Ferramenta

```

```
    
## Arquivos de Configuraçao da Ferramenta


### Config.JSON
    
Arquivo geral de configuração das tarefas de sincronia.
    
Devem ser respeitados padrões de nome para correta leitura dos dados.
    
Nos campos onde caminhos de sistema são passados deve-se respeitar letras maiúsculas e minúsculas, em função das características do sistema operacional Linux que processa estas tarefas.
 
- Tarefa Global
    
Caso algum dos parâmetros das tarefas de sincronia não sejam informados, existe uma tarefa configurada com os parâmetros globais aplicáveis à todas as demais tarefas subsequentes, caso algum valor não tenha sido informado.
    
Exemplo de configuração da tarefa global.

```json
"GLOBAL": {
    "NAME" : "SHARE",
    "DESCRIPTION" : "SHARE DEFAULT.",
    "AUTHOR" : "LBMELLO",
    "ENVIROMENT" : "LINUX",
    "SYNC_LEVEL" : "0",
    "NODE" : "MASTER",
    "SOURCE" : "/tmp/share",
    "USER" : "root",
    "DESTINY" : "/tmp/share",
    "TIME": "DEFAULT"
}
```

#### Parâmetros aplicáveis às Tarefas de Sincronia
 
Representa os valores a serem configurados nas tarefas de sincronia. Várias tarefas podem ser configuradas no mesmo servidor, apenas criando uma nova entrada na lista SHARE.
 
- **NANE** -- Nome do compartilhamento. Informação utilizada para organização das tarefas dentro do sistema. Pode utilizar caracteres alfanuméricos, diferenciando letras maiúsculas de minúsculas.
        
- **DESCRIPTION** -- Descrição do compartilhamento. Informação utilizada para facilitar a identificação do conteúdo das tarefas de sincronia.
        
- **AUTHOR** -- Autor da Tarefa. Identificação do operador que configurou a tarefa dentro do sistema.
        
- **ENVIROMENT** -- (AINDA SEM USO) Sistema operacional onde a ferramenta será executada. Até o presente momento, só existe compatibilidade com ambientes Linux.
        
- **SYNCEVEL** -- (AINDA SEM USO) Nível de sincronia do nó dentro da árvore do compartilhamento. Isso definirá após a implantação, se o nó está iniciando o cenário de ondas ou recebendo os dados de seus antecessores.
        
- **NODE** -- (AINDA SEM USO) Identificação do tipo do nó (master} ou client}).
        
- **SOURCE** -- Diretório de origem dos arquivos. Aonde os arquivos serão localizados localmente para envio aos demais nós da rede. Utilizado também o padrão case sensitive para os diretórios. 
        
- **USER** -- Usuário SSH utilizado para cópia. Existe necessidade da existência deste mesmo usuário no host} de destino, necessita também realizar troca de chaves SSH entre os sistemas para não existir necessidade de incluir a senha durante as sincronias de arquivos.
        
- **IP** -- Endereço de IP da máquina destino.
        
- **DESTINY** -- Diretório de destino dos arquivos na estação remota. Caso o diretório não exista no destino, o mesmo será criado.
        
- **TIME** -- Configuração de tempo para a tarefa. Diretamente conectado com as janelas de tempo criadas no arquivo Time.JSON. O valor declarado nesse parâmetro deve sempre existir no arquivo Time.JSON.

```json
"SHARE": [
    {
        "ID" : "001",
        "NAME" : "TST01", 
        "DESCRIPTION" : "Teste_do_Projeto",
        "AUTHOR" : "LBMELLO",
        "ENVIROMENT" : "LINUX",
        "SYNC_LEVEL" : "0",
        "NODE" : "MASTER",
        "SOURCE" : "/tmp/sharemod",
        "USER" : "fs",
        "DESTINY" : "/tmp/rsync/",
        "TIME" : "24x7&1HS"
    }
```

### Time.JSON
        
Arquivo onde são setadas as configurações das janelas de tempo utilizadas nas tarefas de sincronia. 
    
As configurações de tempo criadas neste arquivo são mencionadas no arquivo Config.JSON, no item *TIME* para agendamento da tarefa de sincronia.
        
Utiliza-se uma sequência lógica entre os valores na montagem do padrão de tempo. Em *OPERATION-TYPE* definimos como queremos executar esta tarefa, em *FREQUENCY* definimos um número que indicará a quantidade de execuções ou repetições, em *TIMEUNITY* definimos uma unidade temporal para esta execução. Finalmente em *SCHEDULE* definimos quais dias da semana a tarefa é executada.
        
- *OPERATION-TYPE* -- Tipo de operação de tempo, indicando a frequência de execução da tarefa. Este parâmetro define como o sistema tratará a execução da tarefa.  
    - *EVERY* -- Caso indicado em *EVERY* a tarefa será executada na modalidade "a cada", o que significa que o valor do campo *FREQUENCY* será considerado juntamente com o campo *TIMEUNITY* para definir a janela de tempo da tarefa. <br/>
	Ex.: Execução agendada a cada 10 minutos:
		*OPERATION-TYPE* = EVERY <br/>
		*FREQUENCY* = 10 <br/>
		*TIMEUNITY* = MINUTE <br/>

    - *JUST* -- Caso indicado em *JUST* a tarefa será executada na modalidade "somente", que pode ser declarada para execuções pontuais, em determinados dias da semana ou horários específicos. <br/>
    Ex.: Execução agendada somente às quartas e sextas-feiras 
	*OPERATION-TYPE* = JUST <br/>
	*SCHEDULE*= __W_F__ <br/>

    - *ONCE* -- Execução realizada somente uma vez, em uma data definida.

    - *SPECIAL* -- Caso o operador special seja informado, o parâmetro *TIME_UNITY* poderá ser suprimido e os operadores especias podem ser usados.
    São eles: *HOURLY* (a cada hora), *DAILY* (diariamente), *WEEKLY* (semanalmente), *MONTHLY* (mensalmente) e *REBOOT* (a cada reiniciada do host).

    - *FREQUENCY* -- Frequência de execução. Declarado sempre com um numeral inteiro, pois isto definirá quantas vezes a tarefa será executada, dependendo dos demais parâmetros.
                
    - *TIME_UNITY* -- Unidade de tempo utilizada nas operações, pode ser *MINUTE* HOUR, DAY, WEEK e MONTH.
        
    - *SCHEDULE* -- Dias da semana que a tarefa será executada, sempre deve ser declarado em maiúsculo, utilizando o padrão de nomenclatura em inglês. 
    
    ```json
            "LAB":{
                "NAME": "LAB",
                "SCHEDULE": "MTWTF__",
                "OPERATOR": "EVERY",
                "FREQUENCY": "5",
                "TIME_UNITY":  "MIN"
            }
        ```
        
**Tempo Global**

Assim como as tarefas de sincronia, existe uma entrada global de tempo cadastrada. Caso nenhum valor seja atribuído nas tarefas de tempo, os valores desta tarefa serão utilizados.
    
```json
        "DEFAULT":{
            "NAME": "DEFAULT",
            "SCHEDULE": "MTWTFSS",
            "OPERATOR": "EVERY",
            "FREQUENCY": "3",
            "TIME_UNITY":  "HRS"
        }
```
    
    
### Hosts.JSON

Arquivo onde os nós da rede devem ser declarados.
        
- *IP* -- Endereço de IP IPV4 da estação/servidor sendo declarado.

- *DESCRIPTION* -- Descrição da estação/servidor para facilitar a identificação daquele nó em inventário.

- *UID* -- Identificação numérica única do nó.

- *SYNC-LEVEL* -- Nível de Sincronia.

- *LEVEL* -- Nome do nível de sincronia sendo declarado.

- *UID* -- Grupo de UIDs pertencentes aquele nível de sincronia.
        
```json
	"NODES": {
        "fs-01": {
			"IP": "192.168.15.100",
			"DESCRIPTION": "cliente fs-01",
			"UID": "001",
            "EDGE": "002"
        }
```

### Domain.JSON

Arquivo onde os dados de doínio são armazenados.
    
- *NAME* - Define-se o nome do domínio
- *DOMAIN_ID* - Define-se o identificador do domínio, listado com o comando ```file-sync --domain list```
- *KNOWN_MEMBER* - IP de algum host conhecido, pertencente ao domínio declarado nos campos acima.

Exemplo do arquivo conf/Domain.JSON:

```json
    {
        "NAME": "lab_domain",
        "DOMAIN_ID": "169a01c91744946f7cb356577200b789",
        "KNOWN_MEMBER": "172.10.0.10"
    }
```

## Uso da Ferramenta via CLI
    
É possível realizar a operação da ferramenta via linha de comando através do módulo CLI. 
    
### sync
        
Gerencia a sessão de sincronia da ferramenta.

Inicia as sincronias de arquivos para todos os *shares*, com o comando:

```
file-sync --sync all
```

Ou inicia somente a sincronia do *share* especificado: 
```
file-sync --sync NOME-DO-SHARE
```
    
### install
    
Faz a instalação das dependências (Python e ambiente virtual) e instala a ferramenta em si no *host*.

Instalação do Python3 mais dependências: 

```sh
file-sync --install python3
```

Instalação da ferramenta:

```sh
file-sync --install
```
    
### crontab
    
Gerencia o módulo cron da ferramenta.

Cria as entradas de execução no *Crontab* para todos os *shares*, com o comando: 

```sh
file-sync --crontab all
```

Ou cria somente as entradas de execução no *Crontab* do *share* especificado: 
```sh
file-sync --crontab NOME-DO-SHARE
```
    
### config
    
Gerencia os dados contidos no arquivo Conf.JSON.

Adiciona uma nova configuração de *share*, solicitando os dados necessários via formulário na sequência de execução do seguinte comando: 

```sh
file-sync --config add
```
        
### domain
    
Administra as interações de domínio, criando um novo domínio e listando as informações do domínio já criado.

Cria domínio novo: 
```sh
file-sync --domain create
```

Lista ID do domínio existente: 
```sh
file-sync --domain list
```
        
## Desenvolvimento Futuro

A fim de complementar o funcionamento da ferramenta, serão desenvolvidos os seguintes itens futuramente:

Envio de dados apenas com alterações entre compartilhamentos
Atualmente a ferramenta gera a árvore de diretórios e arquivos com suas respectivas *hashes* de alteração de arquivos. A ideia é que estes dados sejam trocados entre os nós para comparação do estado de edição dos arquivos. Caso existam diferenças entre a origem e o destino a sincronia será ativada.

Execução da API Desacoplada do Código
A implementação do módulo de API realiza a execução do *framework Flask* em modo de *debug*, dentro do próprio código. Este tipo de implantação é utilizada somente em ambiente de testes, pois impacta em diversos parâmetros e recursos do *framework* ficarem limitados. 
Em função dessa implementação, existe bloqueio de entrada via *Shell*, impossibilitando o uso do módulo CLI.
A ideia em estudo para o futuro é implementar o módulo API desacoplado da execução do projeto, utilizando um servidor web padrão com *fastCgi* ou um container Docker} configurado com o ambiente.

Módulo de Redes
Futuramente será desenvolvido um módulo que testa a qualidade da conexão com os demais *hosts* para identificar os melhores nós possíveis para troca de dados. Estes testes de rede irão considerar se o servidor remoto responde às conexões, se tem boa latência e *jitter* baixo e quantos saltos são realizados até o destino. A informação do melhor nó para troca estará disponível no campo *EDGE* do arquivo Hosts.JSON.
