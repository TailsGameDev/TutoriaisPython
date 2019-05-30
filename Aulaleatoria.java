import java.util.Scanner;

class Tutorial {
  // i = 10  exemplo python
  static int y = 4;
  int z = 5;
  int[] numeros = {2,3,4};
  
  static void funcao() {
    System.out.println("peixe");
  }
  
  public static void main(String[] args) {
    funcao();
    
    float meuFloat = 3.3f;
    String frase = "ola pessoal";
    
    Tutorial t = new Tutorial();
    Tutorial a = new Tutorial();
    //Guerreiro o = new Guerreiro();
    
    int x = 5;
    String meuTexto = "" + x;
    
    if(x > 5){
    	System.out.println("x maior que 5");
    }else if (x >= 0) {
      	System.out.println("x maior ou igual a 0");
    }else if(x != -10){
    	System.out.println("x é diferente de -10");
    }else{
    	System.out.println("x não é 5 nem 10");
    }
    
    int k = 10;
    while(k > 0){
      k = k - 1;
      System.out.println(k);
    }
    
    System.out.println(x+x);
    
    
    System.out.println(meuTexto+meuTexto);
    
    //import java.util.Scanner; lah em cima
    Scanner s = new Scanner(System.in);
    String li = s.nextLine();
    System.out.println(li + " foi lido e impresso");
  }
}
