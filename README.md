#JavaScript参考手册
	*###JavaScript 本地对象和内置对象
	*###Browser对象(BOM)
	*###HTML DOM 对象
##JavaScript对象参考手册
	*Array
	*Boolean
	*Date
	*Math
	*Number
	*String
	*RegExp
	*Global
	##JavaScript Array对象
		###Array对象
			Array对象用于在耽搁边两种存储多个值.
		####闯将Array对象的语法:
		<pre>
			new Array();
			new Aray(size);
			new Array(element0,element1,...,elementn);
		</pre>
		####参数
		参数size是期望的数组元素个数.返回的数组,length字段将被设为size的值.
		参数element...,elementn 是参数列表.当使用这些参数来调用构造函数Array()时,心创建的数组的元素就被初始化为这些值.它的length字段也会被设置为参数的个数.
		####返回值
		返回新创建并被初始化了的数组.
		如果调用构造函数Array()时没有使用参数,那么返回的数组为空,length字段为0.
		当调用构造函数时只传递给它一个数字参数,该构造函数将返回具有制定个数,元素为underfined的数组.
		当其他参数调用Array()时,该构造函数将用参数制定的值初始化数组.
		当把构造函数作为函数调用,不使用new运算符时,它的行为与使用new运算符调用它时的行为完全一样.
		###Array对象属性
		<pre>
			*constructor 返回对创建对象的数组函数的引用.
			*length 设置或返回数组中元素的数目.
			*prototype 使您有能力向对象添加属性和方法.
		</pre>
		####constructor
		#####定义和用法
		constructor属性返回对创建此对象的数组函数的引用.
		#####语法
		<pre>
			object.constructor
		</pre>
		#####实例
		######例子 1
		本例展示constructor属性:
		<pre>
			<script>
			var test = new Aray();

			if(test.constructor==Array) {
				document.write("This is an Array");
			}
			if(test.constructor==Boolean) {
				document.write("This is a Boolean");
			}
			if(test.constructor==Date) {
				document.write("This is a Date");
			}
            if (test.constructor==String) {
            	document.write("This is a String");
            }
			</script>
		</pre>
		###Array对象方法
		*concat() 连接两个或更多的数组,并返回结果.
		*join() 把数组的所有元素放入一个字符串.元素通过制定的分隔符进行分隔.
		*pop() 删除并返回数组的最后一个元素
		*push() 向数组的末尾添加一个或更多元素,并返回新的长度.
		*reverse() 颠倒数组中元素的顺序.
		*shift() 删除并返回数组的第一个元素
		*slice() 从某个已有的数组返回选的元素.
		*sort() 对数组的元素进行排序.
		*splick()删除元素,并向数组添加新元素.