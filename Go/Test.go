package main

import (
	"fmt"
	"reflect"
	"time"
	"strconv"
)

type Abool bool //дефолт обьявляение типа или через =

type Human struct { // Структуры (struct) это коллекция полей. Принято создавать вне main
	Name string
	Alive, WantBecomeTheBest Abool
}

type Homo struct {
	Human
	Gay Abool
}

type MethodsOfHuman interface {
	SayWant() string
	SayHello() string
}

type MethodsOfHomo interface {
	SayWant() string
	SayHello() string
	SayLesbiGay() string
}

func (h Human) SayWant() string { 
	if h.WantBecomeTheBest {
		return "Yes, you suck me"
	}
	return "I am the worst human."
}

func (h Human) SayHello() string { 
	return "Hello, I`am " + h.Name
}

func (h Homo) SayLesbiGay() string { 
	if h.Gay {
		return "I`am Pidor."
	}
	return "I`am Lesbi."
}

func myDef(s string) (a int) {
	a, err := strconv.Atoi(s)
	if err != nil {
		return
	}
	return a
}

func main() {

	massive := [2][2]int{{1, 2}, {3, 4}} //дефолт создания массива

	massive2 := make([]int, 0, 10)

	for i := range massive {
		massive2 = append(massive2, i)
	}

	fmt.Println(massive[0:1], len(massive2), cap(massive2))

	typeIntR := 1
	fmt.Println(reflect.TypeOf(typeIntR)) //получения типа с помощью метода модуля reflect

	switch typeIntR {
	case 1 : // выполнится
		fmt.Println(1) 
		fallthrough // провалюсь до следующего кейса
	case 2 :
		fmt.Println(2) // тоже выполнится, т.к. в первом блоке указан FALLTHROUGH	
	default :
		fmt.Println(3) 
	}

	mapInGo := map[string]string{
		"username" : "ChikiChikiChikiChaka",
		"password" : "DURAK2021$",
	} // дефолт создания карты
	
	fmt.Println("My name is... What? My name is ", mapInGo["username"])

	c1 := make(chan string) // создание потока (канала)
	c2 := make(chan string)

	go func() { //горутины топ ез бот
		time.Sleep(0 * time.Second)
		c1 <- "I am first case."
	}()

	go func() {
		time.Sleep(1 * time.Second)
		c2 <- "I am second case."
	}()

	for i := 0; i < 2; i++ { // буду ждать горутины свыше, а так похуй на их выполнение (проделываем эту операцию 2-ды)
		select { //конченая вещь, SELECT прекращает ожидание при 1-м получении данных, тогда срабатывает CASE 
		case msg1 := <-c1: // происходит DEADLOCK потока при получении данных
			fmt.Println("received", msg1)
		case msg2 := <-c2:
			fmt.Println("received", msg2)
		}
	}

	fmt.Println("Geting values has completed") // будет ждать завершения SELECT

	go func() { //горутины топ ез бот
		time.Sleep(1 * time.Second)
	}()

	go func() {
		time.Sleep(2 * time.Second)
		c2 <- "Di nahui" // в отличии от 1-го потока, в этот мы передали данные (в c1 ничего нет)
	}()

	select { 
	case msg1 := <-c1: // не исполнится т.к. мы не передали дыннаые в горутину
		fmt.Println("GO1->Я какашка.", msg1)
	case msg2 := <-c2:
		fmt.Println("GO2->Свежие единичные данные приняты.", msg2)
	}

	Metka: // обьявляем метку
		for i := 0; i < 10; i++ {
			if (i == 5) {
				break Metka
			} else {
				fmt.Println(i)
				continue Metka
			}
		}

	goto L1; // Утверждение GOTO с меткой L1 обязательно находятся в одном блоке, и код выполнится на месте обьявления GOTO
	L1:
		if (true) {
			fmt.Println("Метка goto выполнена.")
		}

	defer fmt.Println("<---Выход из окружающей среды. (Завершение функции - RETURN)--->") 

	bitSum := 100 | 10 // все побитовы операторы в GO схожи с операторами других языков

	fmt.Println("Побитовая операция сложения 100 и 10 : ", bitSum)

	skibidiWoman := Human{"Huesosovna", true, false}
	man := Human{"Tinker", true, false}
	gayHuman := Homo{man, true} // наследует все implements TYPE Human (включая методы)
	
	fmt.Printf("I`am %v and my status of alive : %s \n", skibidiWoman.Name, skibidiWoman.Alive)

	var interfaceWoman MethodsOfHuman = skibidiWoman // привязывать INTERFACE к STRUCTURE допускается лишь в том случае, когда INTERFACE содержит все методы, которым привязана STRUCTURE

	fmt.Println(interfaceWoman.SayWant())

	interfaceHomo := MethodsOfHomo(gayHuman) // поддерживается следующая вариация записи

	fmt.Println(interfaceHomo.SayHello(), interfaceHomo.SayLesbiGay())
}
