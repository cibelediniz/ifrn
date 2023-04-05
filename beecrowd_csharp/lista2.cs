//Ler o primeiro nome de uma pessoa e mostrar a mensagem: “Bem-vindo ao C#, <xxx>”, onde <xxx> é o nome informado pela pessoa.

using System;

class MainClass { 
    public static void Main() { 
        Console.WriteLine("Digite seu primeiro nome:");
        string nome = Console.ReadLine();
        Console.WriteLine("Bem vindo ao C#, {0}", nome);
    }
}


//Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao C#, <xxx>”, onde <xxx> é o primeiro nome da pessoa.

using System;

class MainClass { 
    public static void Main() { 
        Console.WriteLine("Digite seu nome completo:");
        string[] nome = Console.ReadLine().Split();
        Console.WriteLine($"Bem vindo ao C#, {nome[0]}");
    }
}


//Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3).
//Considerar as notas com valores inteiros entre zero e cem.

using System;

class MainClass { 
    public static void Main() { 
        Console.WriteLine("Digite a nota do primeiro bimestre da disciplina:");
        int nota1 = int.Parse(Console.ReadLine());
        Console.WriteLine("Digite a nota do segundo bimestre da disciplina:");
        int nota2 = int.Parse(Console.ReadLine());
        int media = (nota1 * 2 + nota2 * 3)/5;
        Console.WriteLine($"Média parcial = {media}");
    }
}


//Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. 
//Considerar que os valores podem ser números reais. Mostrar o resultado com duas casas decimais.

using System;

class MainClass { 
    public static void Main() { 
        Console.WriteLine("Digite a base e a altura do retângulo:");
        double b = double.Parse(Console.ReadLine());
        double h = double.Parse(Console.ReadLine());
        
        Console.WriteLine($"Área = {b*h:0.00} - Perímetro = {b*2+h*2:0.00} - Diagonal = {Math.Sqrt(Math.Pow(b,2)+Math.Pow(h,2)):0.00}");
    }
}


//Calcular a distância, em quilômetros, percorrida pela luz em um intervalo de tempo no formato “HH:MM:SS”.
//Considerar a velocidade de luz como 300 mil km/s.

using System;

class DistKm { 
    public static void Main() { 
        Console.WriteLine("Digite o intervalo de tempo no formato “HH:MM:SS”");
        
        string[] hms = Console.ReadLine().Split(":"); //array
        uint h = uint.Parse(hms[0]), m = uint.Parse(hms[1]), s = uint.Parse(hms[2]); //partes do array
        m = m + (h*60); //ou m += h*60
        s = s + (m*60); //ou s += m*60
        Console.WriteLine($"A luz percorreu {300000*s} km nesse intervalo");
    }
}
