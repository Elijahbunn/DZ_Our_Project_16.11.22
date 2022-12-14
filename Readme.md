# Проект "Генерация профилей персонажей"

**_Разработчики_**:
+ Бунин Илья
+ Попов Роман
+ Хоменко Андрей


**_Цель проекта:_** создать приложение-генератор случайных персонажей
с определенным набором характеристик.

**_Актуальность проекта:_** карточки-описания персонажа можно использовать в:
- нейросетях, создающих изображения по описаню;
- ролевых/настольных играх, где каждый игрок должен получить своего уникального персонажа для прохождения;
- компьютерных играх (возможен дальнейший экспорт созданных карточек персонажей во внутреигровую систему создания "рандомных" НПС.


**_Работа приложения:_**
- В папку с файлами приложения добавляется несколько Excel-таблиц, в которых преведены наборы харектеристик и особенностей персонажа, например:
	- Имя;
	- Фамилия;
	- Раса;
	- Возраст;
	- Рост;
	- Одежда;
	- Черты лица;
	- Особенности внешности (шрамы, изъяны, гетерохромия и т.д.);
	- Физические характеристики (сила, ловкость, интеллект и т.д.).

- Из предоставленных Excel-таблиц в рандомном порядке набирается полный набор характеристик, который добавляется в лист (list) в заданной последовательности - по индексу элемента в листе можно определить, какой элемент в нем содержится. Например:
	- имя персонажа находится в list-е под индексом [0].

	- Создаются новые Excel	и MarckDown файлы.

	- Из листа в заданной последовательности "берутся" характеристики
	персонажа и заносятся в новые файлы, которые принимают вид карточек персонажей.

**_Реализованные возможности программирования в данном приложении:_**

+ Разбиение громосткого кода на несколько функциональных частей,
	что дало возможность легко работать с одним приложением нескольким 
	начинающим программистам;

+ Возможность легко изменять и добавлять в приложение функциональные части.
	Например, есть возможность добавить функцию создания карточки персонажа в формате 
	HTML, добавить новые характеристики к уже имеющимся или добавлять к карточкам
	персонажей дополнительные файлы (фото - изображения отдельных частей персонажа, таких как одежда, оружие и т.д.);

+ Экспорт и импорт информации из одного набора файлов в другой, при этом
	сохраняя заданную структуру данных.