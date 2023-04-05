// URI 1009 – Salário com Bônus

using System;

class SalBonus { 
    public static void Main() { 
        string nome = Console.ReadLine();
        double salario = double.Parse(Console.ReadLine());
        double vendas = double.Parse(Console.ReadLine());

        double total = salario + vendas * 0.15;
        
        Console.WriteLine($"TOTAL = R$ {total:0.00}");
    }
}


// URI 1013 – O Maior

using System;
using System.Linq;

class OMaior {
  static void Main() {
    
    int a, b, c, maior;
    int[] nums =  Console.ReadLine().Split().Select(int.Parse).ToArray();
    
    a = nums[0];
    b = nums[1];
    c = nums[2];
    maior = a;
    
    if (b > maior && b > c) {
        Console.WriteLine($"{b} eh o maior");
    }
    
    else if (c > maior && c > b) {
        Console.WriteLine($"{c} eh o maior");
    }
    else{
        Console.WriteLine($"{a} eh o maior");
    }
  }
}


// URI 1014 - Consumo

using System;

class Consumo {
    public static void Main() {
        
        int dist; 
        double gas, gasto;
        
        dist = int.Parse(Console.ReadLine());
        gas = double.Parse(Console.ReadLine());
        gasto = dist / gas;
        Console.WriteLine($"{gasto:0.000} km/l");
    }
}


// URI 1015 - Distância entre dois pontos

using System; 

class DistPont {
    public static void Main(string[] args) { 

        double dist, x, y, x1, x2, y1, y2;
        string linha1, linha2;

        linha1 = Console.ReadLine();
        linha2 = Console.ReadLine();

        string[] i = linha1.Split(' ');
        string[] j = linha2.Split(' ');

        x1 = double.Parse(i[0]);
        y1 = double.Parse(i[1]);
        x2 = double.Parse(j[0]);
        y2 = double.Parse(j[1]);
        
        dist = Math.Sqrt(Math.Pow(x = (x2-x1),2) + Math.Pow(y = (y2-y1),2));

        Console.WriteLine($"{dist:0.0000}");
    }
}


// URI 1018 - Cedulas

using System;
class Cedls {
    public static void Main() {
        int a;
        a = int.Parse(Console.ReadLine());
        
        Console.WriteLine(a);
        
        Console.WriteLine($"{a/100} nota(s) de R$ 100,00");
        a = a - (a/100) * 100;
        
        Console.WriteLine($"{a/50} nota(s) de R$ 50,00");
        a = a - (a/50) * 50;
        
        Console.WriteLine($"{a/20} nota(s) de R$ 20,00");
        a = a - (a/20) * 20;
        
        Console.WriteLine($"{a/10} nota(s) de R$ 10,00");
        a = a - (a/10) * 10;
        
        Console.WriteLine($"{a/5} nota(s) de R$ 5,00");
        a = a - (a/5) * 5;
        
        Console.WriteLine($"{a/2} nota(s) de R$ 2,00");
        a = a - (a/2) * 2;
        
        Console.WriteLine($"{a} nota(s) de R$ 1,00");
    }
}


using System;
using System.Linq;

class Pedagio {
    public static void Main() {
        
        int[] linha1 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int[] linha2 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        
        int km, pedagios, custo_p, custo_t, l, d, k, p;

        l = linha1[0];
        d = linha1[1];
        k = linha2[0];
        p = linha2[1];;
        
        km = k * l;
        pedagios = l/d;
        custo_p = pedagios * p;
        custo_t = custo_p + km;
        
        Console.WriteLine(custo_t);
    }
}
