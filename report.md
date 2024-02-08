# OCR aplicado nas validades
* 13/12/23
* Foi criado um modelo para identificar onde está a validade do produto para de diminuir o tamanho da imagem e aplicar o OCR, a fim de melhorar identificação dos caracteres. 
* As imagens utilizadas para testar o OCR foram as mesmas utilizadas para treinar o modelo. Das 39 imagens disponibilizadas o modelo conseguiu retornar a validade de 34 imagens para serem analisadas pelo OCR.
* 06/02/24
* Foi utilizado uma nova biblioteca para identificar a data de validade dos produtos apresentados, o docTR

## Sobre o treinamento de modelo de reconhecimento de validade
* O modelo foi treinado com YOLOv4
* Inicialmente foram disponibilizadas 51 imagens, sendo:
    * 37 destinadas ao treinamento. (Equivalente a 70% do dataset)
    * 12 destinadas ao teste. (Equivalente a 30% do dataset)
* O intuito do modelo criado é validar a possibilidade de detecção do padrão de validade, a fim de destaca-lo da imagens para que seja aplicado OCR corretamente.
* Portanto, o modelo possui apenas uma classe, sendo:
    * validade
* O modelo foi testado  a partir do comando "darknet map" e obteve uma acuracidade de 60,47%.

## Testes
* Esse foi o resultado dos testes:
### Teste 1
!['teste1'](./test-1.jpg)
#### Output
```
Image test-1
Text: LOTE :3#7720
Text: *00:06/202?
Text: ynl OGvin2s
time expended to read from easyocr: 1.4229247570037842
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-1.png)

### Teste 2
!['teste2'](./test-2.jpg)
#### Output```
```
Image test-2
Text: :;22!401<.:
Text: :12
Text: 22
Text: "n_:12.2^
time expended to read from easyocr: 1.3923704624176025
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-2.png)

### Teste 3
!['teste1'](./test-3.jpg)
#### Output
```
Image test-3
Text: vg8:
time expended to read from easyocr: 0.6015098094940186
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-3.png)

### Teste 5
!['teste1'](./test-5.jpg)
#### Output
```
Image test-5
Text: LOTE
Text: ""1u
Text: |..1".|
Text: FABRICAG4O
Text: VALIDADE
time expended to read from easyocr: 1.3089511394500732
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-5.png)

### Teste 6
!['teste1'](./test-6.jpg)
#### Output
```
Image test-6
Text: IOIL
Text: );
Text: M
Text: FABRICAGGO
Text: VALIDADE
time expended to read from easyocr: 1.1439592838287354
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-6.png)

### Teste 7
!['teste1'](./test-7.jpg)
#### Output
```
Image test-7
Text: z:
Text: t"}
Text: LOTE
Text: u"
Text: mui
Text: a
Text: FABRICAGiO
Text: VALIDADE
time expended to read from easyocr: 2.1793053150177
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-7.png)

### Teste 8
!['teste1'](./test-8.jpg)
#### Output
```
Image test-8
Text: 
Text: ?3
Text: 
Text: 
time expended to read from easyocr: 1.4295597076416016
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-8.png)

### Teste 9
!['teste1'](./test-9.jpg)
#### Output
```
Image test-8
Text: 
Text: ?3
Text: 
Text: 
time expended to read from easyocr: 1.4295597076416016
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-9.png)

### Teste 10
!['teste1'](./test-10.jpg)
#### Output
```
Image test-10
Text: Do8R
Text: 01/2023
Text: r
Text: 12/202!
time expended to read from easyocr: 0.808708906173706
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-10.png)

### Teste 11
!['teste1'](./test-11.jpg)
#### Output
```
Image test-11
Text: Lote:
Text: ABA31&1
Text: Feo.:
Text: 23
Text: ABR
Text: 25
Text: HAR
Text: Val.:
time expended to read from easyocr: 1.9505202770233154
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-11.png)

### Teste 12
!['teste1'](./test-12.jpg)
#### Output
```
Image test-12
Text: ::::
Text: :::` ::::
time expended to read from easyocr: 1.110224962234497
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-12.png)

### Teste 13
!['teste1'](./test-13.jpg)
#### Output
```
Image test-13
Text: L:2305744
Text: F:06/2023
Text: v:06/2025
time expended to read from easyocr: 0.8055934906005859
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-13.png)

### Teste 14
!['teste1'](./test-14.jpg)
#### Output
```
Image test-14
Text: L & 7 0 3 5 5
Text: r
Text: 0 8 /_2 0_2
Text: 0 6 7 2 0 2 5
time expended to read from easyocr: 2.338698387145996
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-14.png)

### Teste 15
!['teste1'](./test-15.jpg)
#### Output
```
Image test-15
Text: f
Text: 0535
Text: 12:4&
Text: :09/23
Text: 0:09/25
time expended to read from easyocr: 1.626593828201294
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-15.png)

### Teste 16
!['teste1'](./test-16.jpg)
#### Output
```
Image test-16
Text: E22!25;;4
Text: :i:
time expended to read from easyocr: 0.7487449645996094
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-16.png)

### Teste 17
!['teste1'](./test-17.jpg)
#### Output
```
Image test-17
Text: L_:82361170
Text: F
Text: 07/23
Text: V:07/25
time expended to read from easyocr: 1.3684864044189453
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-17.png)

### Teste 18
!['teste1'](./test-18.jpg)
#### Output
```
Image test-18
Text: Lote:
Text: Validade:
Text: 2309006
Text: 09/26
Text: |.P:25351.652460/?021-00
time expended to read from easyocr: 2.25237774848938
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-18.png)

### Teste 20
!['teste1'](./test-20.jpg)
#### Output
```
Image test-20
Text: T33
Text: ::::
Text: :_:_
time expended to read from easyocr: 1.4295270442962646
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-20.png)

### Teste 21
!['teste1'](./test-21.jpg)
#### Output
```
Image test-21
Text: 3!77/23
Text: F:05/23
Text: ":05/26
time expended to read from easyocr: 1.236560583114624
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-1.png)

### Teste 22
!['teste1'](./test-22.jpg)
#### Output
```
Image test-22
Text: arp24
Text: urr
Text: 2lll
Text: ng
time expended to read from easyocr: 1.5626583099365234
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-22.png)

### Teste 23
!['teste1'](./test-23.jpg)
#### Output
```
Image test-23
Text: arNen
Text: :::::: !
Text: 322
Text: 53
Text: ..:
time expended to read from easyocr: 2.810075283050537
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-23.png)

### Teste 24
!['teste1'](./test-24.jpg)
#### Output
```
Image test-24
Text: 02723
Text: FPE
Text: 1723
time expended to read from easyocr: 1.2412688732147217
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-24.png)

### Teste 26
!['teste1'](./test-26.jpg)
#### Output
```
Image test-26
Text: 10/2025 05 39
Text: VAL
Text: BRO22
Text: L0TE051023
time expended to read from easyocr: 0.9443676471710205
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-26.png)

### Teste 27
!['teste1'](./test-27.jpg)
#### Output
```
Image test-27
time expended to read from easyocr: 0.07843208312988281
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-27.png)

### Teste 29
!['teste1'](./test-29.jpg)
#### Output
```
Image test-29
Text: IL IA IDI F
Text: UI26
time expended to read from easyocr: 0.9187045097351074
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-29.png)

### Teste 30
!['teste1'](./test-30.jpg)
#### Output
```
Image test-30
Text: LY209?
Text: @1|26
Text: 25051.537577/
Text: a
time expended to read from easyocr: 2.072737693786621
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-30.png)

### Teste 31
!['teste1'](./test-31.jpg)
#### Output
```
vImage test-31
Text: :__74!4;:424
Text: _
Text: ;;;
Text: !:ji:
time expended to read from easyocr: 1.6173803806304932
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-31.png)

### Teste 32
!['teste1'](./test-32.jpg)
#### Output
```
Image test-32
Text: geroo
Text: 8%9
Text: 
Text: coo
Text: "8
Text: !
Text: 8
Text: Gre
Text: Qoc
Text: c
Text: Qo
Text: e
Text: ce
Text: ee
Text: ca
Text: ccsco
Text: oo
Text: csco
Text: ccu
Text: ce0
Text: ceL
Text: ca
Text: ccaeo
Text: cee
Text: co
Text: %
Text: Gl
Text: eao
Text: &cco
Text: eceo
Text: L
Text: Cau@
Text: a
Text: TtIF
Text: Ree
Text: Gao
Text: oco
Text: edo
Text: gssco
Text: ceo
Text: &s~=
Text: !!1
Text: I!F:
Text: caeo
Text: eoc8
Text: ege
Text: c8
Text: coo
Text: 6c8
Text: cee
time expended to read from easyocr: 11.407180070877075
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-32.png)

### Teste 33
!['teste1'](./test-33.jpg)
#### Output
```
Image test-33
Text: .;_=::!:{4.
Text: :g:_:
Text: _
Text: 4:
Text: -=
Text: jii
Text: i:
Text: :irii
time expended to read from easyocr: 3.029630184173584
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-33.png)

### Teste 34
!['teste1'](./test-34.jpg)
#### Output
```
Image test-34
Text: *._`;10
Text: 0 512 2
Text: F
Text: c 5 [ 2 4
time expended to read from easyocr: 2.051262140274048
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-34.png)

### Teste 35
!['teste1'](./test-35.jpg)
#### Output
```
Image test-35
Text: ai&
Text: fn
time expended to read from easyocr: 0.7180731296539307
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-35.png)

### Teste 37
!['teste1'](./test-37.jpg)
#### Output
```
Image test-37
Text: 17525803
Text: LOT
Text: 06/26
Text: VAL
time expended to read from easyocr: 1.3817987442016602
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-37.png)


### Teste 38
!['teste1'](./test-38.jpg)
#### Output
```
Image test-38
time expended to read from easyocr: 0.32848143577575684
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-38.png)

### Teste 39
!['teste1'](./test-39.jpg)
#### Output
```
Image test-39
Text: 3161!!X?11_
Text: 7"? =
Text: C?
Text: FAB.!G
Text: LOTE:/
Text: VAL.:/EXP.:
time expended to read from easyocr: 2.3123295307159424
```
#### Google Cloud Vision AI
!['vision ai'](../google-cloud-try-api/test-39.png)

## Avaliação
* Foram utilizados dois algoritmos de OCR, o pytesseract e o easyOCR. Entretanto, apenas o easyOCR retornou resultados.
* O maior problema do easyOCR está na identificação de caracteres onde os caracteres são formados por pontos. Ele não é capaz de identificar sendo um ponto. Trabalhos de pré-processamento estão sendo realizados para superar esse desafio.
* A ferramenta Google Cloud Vision AI é extremamente acurada.
