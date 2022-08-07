# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


ar i=0,input,flg
//7,7,t		8,5,f	7,3,f	0,0,f
test(["-a+a-aa","-a+aa-aa","-a+b-aa",""],s1)

//0,0,t 	10,10,t,	5,5,f	4,2,f	5,2,f
test(["","((())())()","(())(","())(","((0))"],s2)

//0,0,f		4,2,f	1,0,f	5,5,f	6,6,t	1,0,f
test(["","0101","1","00011","000111",'0'],s3)

function test(list,fn){
	for(let j=0;j<list.length;j++){
		i=0
		flg=true
		input=list[j]
		fn()
		console.log(input.length,input,i,flg&&i==input.length)
	}
}

function error(){
	flg=false
	console.log("syntax error at"+i)
	//throw Error("syntax error at"+i)		//注释掉会有逻辑错误
}

function match(c){
	if(c==input[i]){
		i=i+1
	}else{
		error()
	}
}
//S->+SS|-SS|a
function s1(){
	let c=input[i]
	switch(c){
		case("+"):match("+");s1();s1();break
		case("-"):match("-");s1();s1();break
		case("a"):match("a");break
		default:error()
	}
}

//S->S(S)S|ε
function s2(){
	if(input=='')return
	let c=input[i]
	if(c=="("){
		match("(")
		s2()
		match(")")
		s2()
	}else{
		//error()			//不需要,因为可以匹配ε
	}
}

//S->0S1|01:method1
function s3(){
	let c=input[i]
	if(c=="0"){
		match("0")
		if(input[i]=='0')s3()
		match("1")
	}else{
		error()
	}
}

//S->0S1|01:method2
function s3(){
	let c=input[i]
	if(c=="0"){
		match("0")
		s3()
		match("1")
	}else if(c=="1"){
		//do nothing
	}else{
		error()
	}
}
