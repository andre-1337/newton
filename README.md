# Newton

A new, experimental high-level toy programming language that is statically-typed, object-oriented and compiles to C. What a mouth full.

## The purpose of Newton

That header was a mouth full, eh? Newton serves as a programming language, with the versatility of, say, C# or Java, while compiling down to C, making it faster than both those languages. Newton's syntax is very C-like, but provides a lot of niceties that C does not have. These niceties can be boiled down to a more readable syntax, with higher level constructs, while still providing manual management over the memory of the application.

## That's cool and all, but can we actually see some syntax that proves all that?

Sure!

```rs
from std.io import println;

enum Animal {
	Cat,
	Dog,
	Cow
}

trait AnimalBehavior {
	fn new(&self): Self => self;

	fn getAnimalType(): abstract Animal;
	fn getAnimalSound(): abstract string;
}

struct Cat implements AnimalBehavior {
	fn getAnimalType(): Animal => Animal.Cat;

	fn getAnimalSound(): string => "Meow!";
}

struct Dog implements AnimalBehavior {
	fn getAnimalType(): Animal => Animal.Dog;

	fn getAnimalSound(): string => "Woof!";
}

struct Cow implements AnimalBehavior {
	fn getAnimalType(): Animal => Animal.Cow;

	fn getAnimalSound(): string => "Moo!";
}

fn main(argc: int, argv: string[]): int {
	let animal = new Cat();
	println(animal.getAnimalSound());

	return 0;
}
```

Hopefully this is enough for you!

## When can I use Newton?

There is currently no ETA on a fully functioning Newton compiler. The first iterations will most likely be very buggy, but we hope to have something somewhat working in the near future
