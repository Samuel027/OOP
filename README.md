# Object Oriented Programming - Real-world problem modelling

A repository that demonstrates a real-world problem modeled using Object Oriented Programming while taking advantage of inheritance, encapsulation, polymorphism and other Object Oriented Programming concepts

## Polymorphism

Polymorphism is the characteristic of being able to assign a different meaning or usage to something in different contexts - specifically, to allow an entity such as a variable, a function, or an object to have more than one form. Polymorphism is demonstrated when the `get_model` method in the childclass of Desktop overwrites the parent class of `Computer`

## Encapsulation

Encapsulation is a concept that binds together the data and functions that manipulate the data, and that keeps both safe from outside interference and misuse. Encapsulation is demonstrated by the private method `_get_battery_status` and the public method `get_battery_status` where the information on the former method is not apparent

## Inheritance

Inheritance enables new objects to take on the properties of existing objects. In this case `laptop` and `desktop` childclasses inherit properties from the parentclass `Computer`

## Parent-class

The parent-class is a class which gives a method or methods to a python child-class. In this example, `Computer`

## Child-class

Inheritance enables new objects to take on the properties of existing objects. In this example `Laptop` and `Desktop` child-classes inherit properties from the parent-class computer
