# Resultados do desafio OCR

* 07/02/24
* A biblioteca utilizada para os novos testes foi a DocTR
* Foi utilizado um modelo pré-treinado para identificar onde está a validade do produto
* Para o teste foram usadas 50 imagens com diferentes tipos de fontes e iluminações a fim de concluir o comportamento amplo da biblioteca
* As imagens foram testadas usando dois parametros do modelo, assume_straight_pages=True/False

## Conclusões

* Das 50 imagens conclui-se que 
	- A ferramenta do Google Cloud Vision API reconheceu 41 datas certas
	- O modelo docTR reconheceu 36 datas certas
* A biblioteca docTR trabalha melhor com imagens não manipuladas
* O reconhecimento é mais preciso com o parâmento assume_straight_pages=True, logo, é mais preciso quando a data está horizontal
* A ferramenta Google Cloud Vision API mudou a posição da imagem e as boxes ficaram descentralizadas com o texto visualmente
* Ambas ferramentas têm maior precisão com os textos focalizados

## Testes

Segue o resultado dos testes

### Teste 1

#### DocTR
!['teste1'](./new_results/images/Figure_1.png)
!['teste1'](./new_results/images2/Figure_1.png)
#### Google Cloud Vision API
!['teste1'](./google_api/result_api1.png)


### Teste 2

#### DocTR
!['teste2'](./new_results/images/Figure_2.png)
!['teste2'](./new_results/images2/Figure_2.png)
#### Google Cloud Vision API
!['teste2'](./google_api/result_api2.png)

### Teste 3

#### DocTR
!['teste3'](./new_results/images/Figure_3.png)
!['teste3'](./new_results/images2/Figure_3.png)
#### Google Cloud Vision API
!['teste3'](./google_api/result_api3.png)

### Teste 4

#### DocTR
!['teste4'](./new_results/images/Figure_4.png)
!['teste4'](./new_results/images2/Figure_4.png)
#### Google Cloud Vision API
!['teste4'](./google_api/result_api4.png)


### Teste 5

#### DocTR
!['teste5'](./new_results/images/Figure_5.png)
!['teste5'](./new_results/images2/Figure_5.png)
#### Google Cloud Vision API
!['teste5'](./google_api/result_api5.png)

### Teste 6

#### DocTR
!['teste6'](./new_results/images/Figure_6.png)
!['teste6'](./new_results/images2/Figure_6.png)
#### Google Cloud Vision API
!['teste6'](./google_api/result_api6.png)

### Teste 7

#### DocTR
!['teste7'](./new_results/images/Figure_7.png)
!['teste7'](./new_results/images2/Figure_7.png)
#### Google Cloud Vision API
!['teste7'](./google_api/result_api7.png)

### Teste 8

#### DocTR
!['teste8'](./new_results/images/Figure_8.png)
!['teste8'](./new_results/images2/Figure_8.png)
#### Google Cloud Vision API
!['teste8'](./google_api/result_api8.png)

### Teste 9

#### DocTR
!['teste9'](./new_results/images/Figure_9.png)
!['teste9'](./new_results/images2/Figure_9.png)
#### Google Cloud Vision API
!['teste9'](./google_api/result_api9.png)

### Teste 10

#### DocTR
!['teste10'](./new_results/images/Figure_10.png)
!['teste10'](./new_results/images2/Figure_10.png)
#### Google Cloud Vision API
!['teste10'](./google_api/result_api10.png)

### Teste 11

#### DocTR
!['teste11'](./new_results/images/Figure_11.png)
!['teste11'](./new_results/images2/Figure_11.png)
#### Google Cloud Vision API
!['teste11'](./google_api/result_api11.png)

### Teste 12

#### DocTR
!['teste12'](./new_results/images/Figure_12.png)
!['teste12'](./new_results/images2/Figure_12.png)
#### Google Cloud Vision API
!['teste12'](./google_api/result_api12.png)

### Teste 13

#### DocTR
!['teste13'](./new_results/images/Figure_13.png)
!['teste13'](./new_results/images2/Figure_13.png)
#### Google Cloud Vision API
!['teste13'](./google_api/result_api13.png)

### Teste 14

#### DocTR
!['teste14'](./new_results/images/Figure_14.png)
!['teste14'](./new_results/images2/Figure_14.png)
#### Google Cloud Vision API
!['teste14'](./google_api/result_api14.png)

### Teste 15

#### DocTR
!['teste15'](./new_results/images/Figure_15.png)
!['teste15'](./new_results/images2/Figure_15.png)
#### Google Cloud Vision API
!['teste15'](./google_api/result_api15.png)

### Teste 16

#### DocTR
!['teste16'](./new_results/images/Figure_16.png)
!['teste16'](./new_results/images2/Figure_16.png)
#### Google Cloud Vision API
!['teste16'](./google_api/result_api16.png)

### Teste 17

#### DocTR
!['teste17'](./new_results/images/Figure_17.png)
!['teste17'](./new_results/images2/Figure_17.png)
#### Google Cloud Vision API
!['teste17'](./google_api/result_api17.png)

### Teste 18

#### DocTR
!['teste18'](./new_results/images/Figure_18.png)
!['teste18'](./new_results/images2/Figure_18.png)
#### Google Cloud Vision API
!['teste18'](./google_api/result_api18.png)

### Teste 19

#### DocTR
!['teste19'](./new_results/images/Figure_19.png)
!['teste19'](./new_results/images2/Figure_19.png)
#### Google Cloud Vision API
!['teste19'](./google_api/result_api19.png)

### Teste 20

#### DocTR
!['teste20'](./new_results/images/Figure_20.png)
!['teste20'](./new_results/images2/Figure_20.png)
#### Google Cloud Vision API
!['teste20'](./google_api/result_api20.png)

### Teste 21

#### DocTR
!['teste21'](./new_results/images/Figure_21.png)
!['teste21'](./new_results/images2/Figure_21.png)
#### Google Cloud Vision API
!['teste21'](./google_api/result_api21.png)

### Teste 22

#### DocTR
!['teste22'](./new_results/images/Figure_22.png)
!['teste22'](./new_results/images2/Figure_22.png)
#### Google Cloud Vision API
!['teste22'](./google_api/result_api22.png)

### Teste 23

#### DocTR
!['teste23'](./new_results/images/Figure_23.png)
!['teste23'](./new_results/images2/Figure_23.png)
#### Google Cloud Vision API
!['teste23'](./google_api/result_api23.png)

### Teste 24

#### DocTR
!['teste24'](./new_results/images/Figure_24.png)
!['teste24'](./new_results/images2/Figure_24.png)
#### Google Cloud Vision API
!['teste24'](./google_api/result_api24.png)

### Teste 25

#### DocTR
!['teste25'](./new_results/images/Figure_25.png)
!['teste25'](./new_results/images2/Figure_25.png)
#### Google Cloud Vision API
!['teste25'](./google_api/result_api25.png)

### Teste 26

#### DocTR
!['teste26'](./new_results/images/Figure_26.png)
!['teste26'](./new_results/images2/Figure_26.png)
#### Google Cloud Vision API
!['teste26'](./google_api/result_api26.png)

### Teste 27

#### DocTR
!['teste27'](./new_results/images/Figure_27.png)
!['teste27'](./new_results/images2/Figure_27.png)
#### Google Cloud Vision API
!['teste27'](./google_api/result_api27.png)

### Teste 28

#### DocTR
!['teste28'](./new_results/images/Figure_28.png)
!['teste28'](./new_results/images2/Figure_28.png)
#### Google Cloud Vision API
!['teste28'](./google_api/result_api28.png)

### Teste 29

#### DocTR
!['teste29'](./new_results/images/Figure_29.png)
!['teste129'](./new_results/images2/Figure_29.png)
#### Google Cloud Vision API
!['teste29'](./google_api/result_api29.png)

### Teste 30

#### DocTR
!['teste30'](./new_results/images/Figure_30.png)
!['teste30'](./new_results/images2/Figure_30.png)
#### Google Cloud Vision API
!['teste30'](./google_api/result_api30.png)

### Teste 31

#### DocTR
!['teste31'](./new_results/images/Figure_31.png)
!['teste31'](./new_results/images2/Figure_31.png)
#### Google Cloud Vision API
!['teste31'](./google_api/result_api31.png)

### Teste 32

#### DocTR
!['teste32'](./new_results/images/Figure_32.png)
!['teste32'](./new_results/images2/Figure_32.png)
#### Google Cloud Vision API
!['teste32'](./google_api/result_api32.png)

### Teste 33

#### DocTR
!['teste33'](./new_results/images/Figure_33.png)
!['teste33'](./new_results/images2/Figure_33.png)
#### Google Cloud Vision API
!['teste33'](./google_api/result_api33.png)

### Teste 34

#### DocTR
!['teste34'](./new_results/images/Figure_34.png)
!['teste34'](./new_results/images2/Figure_34.png)
#### Google Cloud Vision API
!['teste34'](./google_api/result_api34.png)

### Teste 35

#### DocTR
!['teste35'](./new_results/images/Figure_35.png)
!['teste35'](./new_results/images2/Figure_35.png)
#### Google Cloud Vision API
!['teste35'](./google_api/result_api35.png) 


### Teste 36
      
#### DocTR
!['teste36'](./new_results/images/Figure_36.png)
!['teste36'](./new_results/images2/Figure_36.png)
#### Google Cloud Vision API
!['teste36'](./google_api/result_api36.png)



### Teste 37
      
#### DocTR
!['teste37'](./new_results/images/Figure_37.png)
!['teste37'](./new_results/images2/Figure_37.png)
#### Google Cloud Vision API
!['teste37'](./google_api/result_api37.png)



### Teste 38
      
#### DocTR
!['teste38'](./new_results/images/Figure_38.png)
!['teste38'](./new_results/images2/Figure_38.png)
#### Google Cloud Vision API
!['teste38'](./google_api/result_api38.png)



### Teste 39
      
#### DocTR
!['teste39'](./new_results/images/Figure_39.png)
!['teste39'](./new_results/images2/Figure_39.png)
#### Google Cloud Vision API
!['teste39'](./google_api/result_api39.png)



### Teste 40
      
#### DocTR
!['teste40'](./new_results/images/Figure_40.png)
!['teste40'](./new_results/images2/Figure_40.png)
#### Google Cloud Vision API
!['teste40'](./google_api/result_api40.png)



### Teste 41
      
#### DocTR
!['teste41'](./new_results/images/Figure_41.png)
!['teste41'](./new_results/images2/Figure_41.png)
#### Google Cloud Vision API
!['teste41'](./google_api/result_api41.png)



### Teste 42
      
#### DocTR
!['teste42'](./new_results/images/Figure_42.png)
!['teste42'](./new_results/images2/Figure_42.png)
#### Google Cloud Vision API
!['teste42'](./google_api/result_api42.png)



### Teste 43
      
#### DocTR
!['teste43'](./new_results/images/Figure_43.png)
!['teste43'](./new_results/images2/Figure_43.png)
#### Google Cloud Vision API
!['teste43'](./google_api/result_api43.png)



### Teste 44
      
#### DocTR
!['teste44'](./new_results/images/Figure_44.png)
!['teste44'](./new_results/images2/Figure_44.png)
#### Google Cloud Vision API
!['teste44'](./google_api/result_api44.png)



### Teste 45
      
#### DocTR
!['teste45'](./new_results/images/Figure_45.png)
!['teste45'](./new_results/images2/Figure_45.png)
#### Google Cloud Vision API
!['teste45'](./google_api/result_api45.png)



### Teste 46
      
#### DocTR
!['teste46'](./new_results/images/Figure_46.png)
!['teste46'](./new_results/images2/Figure_46.png)
#### Google Cloud Vision API
!['teste46'](./google_api/result_api46.png)



### Teste 47
      
#### DocTR
!['teste47'](./new_results/images/Figure_47.png)
!['teste47'](./new_results/images2/Figure_47.png)
#### Google Cloud Vision API
!['teste47'](./google_api/result_api47.png)



### Teste 48
      
#### DocTR
!['teste48'](./new_results/images/Figure_48.png)
!['teste48'](./new_results/images2/Figure_48.png)
#### Google Cloud Vision API
!['teste48'](./google_api/result_api48.png)



### Teste 49
      
#### DocTR
!['teste49'](./new_results/images/Figure_49.png)
!['teste49'](./new_results/images2/Figure_49.png)
#### Google Cloud Vision API
!['teste49'](./google_api/result_api49.png)



### Teste 50
      
#### DocTR
!['teste50'](./new_results/images/Figure_50.png)
!['teste50'](./new_results/images2/Figure_50.png)
#### Google Cloud Vision API
!['teste50'](./google_api/result_api50.png)
