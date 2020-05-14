# 0512 JavaScript

#### 변수선언

* let (재정의x 재할당o, block scope)

  변수 선언. 한번만 선언할 수 있다.

  let a =3 

  a = 4 재할당 가능

* const (재정의x 재할당 o, block scope)

  변수 선언. 항상 값을 넣어줘야 한다. 해당 명칭으로 한번만 선언가능(재정의불가).  const a=3

  재할당불가 a = 4 (x)

* var (재정의o, 재할당 x, function scope, ES6부턴 사용 x)

  재정의, 재할당 둘다 가능

  전역변수처럼 사용됨 (호이스팅특성을 가짐)

![](C:\Users\tgb03\Desktop\TIL\JS\기본문법\var는 전역변수처럼 사용됨.PNG)

* let vs const

let : 재할당 가능

const : 재할당 불가능 !== 값이 바뀌지 않는다.(e.g. 배열을 할당했는데 배열에 값 추가-> 재할당하진 않았지만 배열은 변했다.)

---

## 1. 타입과 연산자 

### Primitive 타입



#### Number

* NaN : Not a Number



#### String

* template literal

  ``` ` (back틱) 사용 -> 줄바꿈 가능

```javascript
const sent2 = `Hi
world`
줄바꿈 가능
const sent1 = "hi
world" 줄바꿈 불가 ->undefined

const abc2 = `안녕 월드 영어는: ${sent2}`

```



#### Boolean



#### Empty

* Null : 개발자 인위적 값이 없음 나타냄
* undefined : JS에서 값이 없음을 나타내는 자동 할당값

* null vs undefined

```javascript
일반 비교
null == undefined : true

엄격한 비교
null === undefined : False

typeof undefined
"undefined"

typeof null
"object" -> 오류(실수)
고치지 않은 이유: 기존 null타입에 의존하고 있는 웹프로그램들이 망가질까봐. 영향미칠까봐 고치지 못했음.
```



### 연산자

#### 할당연산자

* +=, -=, *=, ++, --

#### 비교연산자

* < , > ,<= ,>=

#### 동등연산자

* ==

#### 일치연산자

* === :엄격한 연산자

#### 논리연산자

* 단축평가처럼 작용
* and (&&)
* or (||)
* not (!)

#### 삼항연산자

* A if 조건 else B -> 참이면 a가 거짓이면 b가 리턴됌. (파이썬)

* `조건? A : B` : 조건이 참이면 A가 거짓이면 B가 리턴됌



---

## 2. 조건문과 반복문

### 조건문

* if, else if , else

```javascript
let day = 7

if (day === 1 ){
    console.log('월요일')
}else if (day===2){
    console.log('화요일')
}else if (day===3){
    console.log('수요일')
}else if (day===4){
    console.log('목요일')
}else if (day===5){
    console.log('금요일')
}else if (day===6){
    console.log('토요일')
}else {
    console.log('일요일')
}

```

* switch

```javascript
let day = 7

switch(day){
    case 1:{
        console.log('월요일')
        break
    }
    case 2:{
        console.log('화요일')
        break
    }
    case 3:{
        console.log('수요일')
        break
    }
    case 4:{
        console.log('목요일')
        break
    }
    case 5:{
        console.log('금요일')
        break
    }
    case 6:{
        console.log('토요일')
        break
    }
    default:{
        console.log('일요일') 
    }
}
```

### 반복문

* while

```javascript
let cnt = 0
while(cnt <=5){
console.log(cnt++)
}
```

* for

```javascript
for (let i=0; i<6; i++){
    console.log(i)
}
```

* for ... of 

__object형태는 사용 불가__

```javascript
const numbers = [0,1,2,3,4]

for (const number of numbers){
    console.log(number)
}
```

* for ... in

__object형태는 사용 가능__

```javascript
const fruits = {
    'apple':2,
    'banana': 10,
    'tomato': 10,
    'watermelon':2,
}

for (const f in fruits){
    console.log(f)
}

for (const f in fruits){
    console.log(`${f} : ${fruits[f]}`)
}
```

__array형태도 사용가능 그러나 index값이 들어간다.__

```javascript
const a = ['a','b','c']

for (const c in a){
    console.log(c)
}
결과
0
1
2
```

* continue

> for문과 continue를 활용하여 0~9중 3제외한 모든 숫자 출력

```javascript
for (let i=0; i<10; i++){
    if (i===3){
        continue
    }
    console.log(i)
}
```

----

## 3. 함수

### 선언식 & 표현식

funciton사용.(파이썬의 def같은)

#### 선언식 

함수이름 쓰는 것 (add)

> function add(num1, num2){
>
> return num1+num2
>
> }

#### 표현식 

변수에 담아두고, 변수이름 호출->함수실행, 익명으로 주로 선언됨.

1. 함수이름 없는 경우. 익명선언(일반적)

> const sub = function(num1,num2){
>
> ​	return num1-num2
>
> }
>
> sub(5,3) 

2. 함수 이름 있는 경우 - 오류추적 유리

>const sub2 = function mySub(num1,num2){
>
>return num1-num2}
>
>sub(6,4)

### 화살표함수(=>)

* __항상 익명이다__
* 생성자로 사용할 수 없다.
* 구문이 짧다.
* this, arguments, super 키워드를 사용할 수 없다.

__일반함수에서 화살표함수로 변환하는 단계__

> 1단계 : function keyword 삭제하고 화살표
>
> ```javascript
> const greeting = (name) => {
> 
>  	return `hello ${name}`
> 
> }
> ```
>
> 2단계 : 매개변수가 하나라면 ( )생략, 그러나 default값 있으면 생략불가
>
> ```javascript
> const greeting = name => {
> 
>  return `hello ${name}`
> 
> }
> //그러나 default값 있으면 생략불가
> let sayHi = (name='펭수')=> `Hi ${name}`
> ```
>
> 3단계 : 바디에 표현식이 한개만 있다면 return과 {}를 생략할 수 있다.
>
> ```javascript
> const greeting = name => `hello ${name}`
> 
> 변수 2개일 때.
> const greeting = (name,name2) => `hello ${name} ${name2}`
> ```

* arrowfunc.js 파일 예시

```javascript

const greeting = function(name){
    return `hello ${name}`
}
console.log(greeting('정승희'))
```

실행방법

`node arrowfunc.js`

#### 실습

* 정사각형 만들기

```javascript
let square = function(num){
    return num**2
}

let square = num => num**2
```



* 아규먼트가 없을 때

```javascript
let noArg = function() {
    return '아규먼트가 없으요'
}
console.log(noArg()) 로 확인

1. let noArg = () => '아규먼트가 없어요'
2. let noArg = _ => '아규먼트가 없어요'
```

* object 리턴하는 함수 -> 

  __object는 리턴할때 괄호씌워야__

```javascript
let returnObj = function (value) {
    return {'key':value}
}
//1단계
let returnOnj = (value) => {return {'key':value}}
//2단계
let returnObj = value => {return {'key':value}}
//3단계
let returnObj = value => {'key':value}
console.log(returnObj(1000))

//정답:
let returnObj = value => ({'key':value})
console.log(returnObj(1000))
```

* 변수가 2개인 경우

```javascript

```



---

## 4. 자료구조 (Array&Object)

### 배열(Array)

* 배열의 인덱스 접근(음수불가)

  ```javascript
  const numbers = [1,2,3,4]
  console.log(numbers[0]) 
  console.log(numbers.length) 
  //맨 끝 원소에 접근하고 싶을 때
  console.log(numbers[-1]) //음수접근불가
  console.log(numbers[numbers.length-1]) 
  
  ```

  * 배열의 맨 끝 접근(음수불가-> length이용해야)

  `console.log(numbers[numbers.length-1]) `

* 자주 쓰이는 배열 매서드

  * `reverse`  : `numbers.reverse()`

  * `push` : 맨 뒤에 값 추가. `numbers.push('a') ` push의 결과값은 length.

  * `pop` : 맨 끝 값 삭제하고 가짐.`numbers.pop()` pop된 값이 결과값

  * `shift` : 맨 앞 값 삭제하고 가짐 `numbers.shift()` 맨 앞에 값 배열에서 없애고 결과값으로 출력

  * `unshift` : 맨 앞에 값 추가. `numbers.unshift(4)` 맨 앞에 값 추가하고 총 배열의 길이를 출력

  * `includes` : 배열에 포함되어있는지 확인`numbers.includes(1)` : True, `numbers.includes(0)` : False

  * `indexOf` : 값이 있으면 인덱스 위치, 값 없으면 -1출력 `numbers.indexOf(3)` : 1, `numbers.indexOf(0)` : -1

  * `join` : 각각 ,으로 연결해서 보여줌. 배열은 안바귐

    ,이 디폴트값

    `numbers.join()` : 4,3,2,1

    `numbers.join(_)` : 4_3_2_1

    `numbers.join('')` : 4321



### 오브젝트(Object)

* 오브젝트의 키 값으로 text가능

  ```javascript
  const pengsu ={
      name : '펭수',
      'phone number':'01012345678',
      profile : {
          dream : '우주대스타',
          age : '11살',
          speciality : '요들송',
      }
  }
  
  //키가 ''로 되어있을 때는 무조건 []으로만 접근가능
  console.log(pengsu['phone number'])
  ```

  

* 오브젝트의 value값으로 딕셔너리 가능

* key를 []로 value접근 시 `''`붙여야 : `'key_name'`

```javascript
const pengsu ={
    name : '펭수',
    'phone number':'01012345678',
    profile : {
        dream : '우주대스타',
        age : '11살',
        speciality : '요들송',
    }
}

console.log(pengsu['name'])
//아니면 .속성값으로 접근
console.log(pengsu.name)
//키가 ''로 되어있을 때는 무조건 []으로만 접근가능
console.log(pengsu['phone number'])

console.log(pengsu.profile)
console.log(pengsu.profile.dream)
```

* 아니면 `.속성명`으로 접근

* key, value값 받기

  `Object.keys(pengsu)`, `Object.values(pengsu)`,`Object.entries(pengsu)`

  ```javascript
  //key 받기
  console.log(Object.keys(pengsu))
  //value받기
  console.log(Object.values(pengsu))
  //둘 다 받기
  console.log(Object.entries(pengsu))
  ```

  



---

# Live2

## ES - logic

### 절대 느슨한 일치연산자를 사용하지 않는다. 

* ==,!= (x)
* ===, !== (o)

___

### 컨벤션/스타일 가이드

* 구글 컨벤션
* 에어비엔비 컨벤션(인기많다)

---

### let vs const

* let : 재할당 가능

* const : 재할당 불가능 !== 값이 바뀌지 않는다.(e.g. 배열을 할당했는데 배열에 값 추가-> 재할당하진 않았지만 배열은 변했다.)

---

### Naming Convention 꼭 지키자

* snake case(bad)

  const add_one_to_number (bad)

  

* lowerCamel(good)

  const addOneToNumber (good)

---

### Function => 1급 객체

1. 변수에 저장할 수 있다.
2. 함수의 리턴값이 될 수 있다.
3. 함수의 인자가 될 수 있다.

---

### DOM(Document Object Model)

* Domtree 

> 메모장에서는 그저 string일지라도 브라우저에서는 해석된다. 트리로 탐색.

![](C:\Users\tgb03\Desktop\TIL\JS\기본문법\Dom Tree.PNG)