// Projeto IF Quest
// Aula 4 - POO
// Parte 2 - Herança


// Classe com atributos e comportamentos de cada personagem
public class Personagem {
    private String nome;
    private int vida;
    private int nivel;

    // Construtor padrão
    public Personagem() {
        definirNome("Personagem");
        definirVida(100);
        definirNivel(1);
    }

    // Construtor parametrizado
    public Personagem(String nome, int vida, int nivel) {
        definirNome(nome);
        definirVida(vida);
        definirNivel(nivel);
    }

    public void definirNome(String nome) {
        this.nome = nome;
    }

    public String obterNome() {
        return this.nome;
    }
    
    public void definirVida(int vida) {
        if (vida < 0) {
            this.vida = 0;
        } else if (vida > 100) {
            this.vida = 100;
        } else {
            this.vida = vida;
        }
    }

    public int obterVida() {
        return this.vida;
    }

    public String ficha() {
        return "Nome: " + this.nome + "\nVida: " + this.vida + "\nNível: " + this.nivel;
    }

    public void definirNivel(int nivel) {
        if (nivel < 1) {
            this.nivel = 1;
        } else {
            this.nivel = nivel;
        }
    }

    public int obterNivel() {
        return this.nivel;
    }

    // Método atacar sem parâmetros
    public void atacar() {
        System.out.println(this.nome + " realizou um ataque padrão de 10 de dano.");
    }

    // Método atacar sobrecarregado com dano definido
    public void atacar(int dano) {
        System.out.println(this.nome + " realizou um ataque de " + dano + " de dano.");
    }
}


// Classe Item 
class Item {
    private String nome;
    private int bonus;

    // construtor
    public Item(String nome, int bonus) {
        this.nome = nome;

        // validando bonus
        if (bonus < 0) {
            this.bonus = 0;
        }
        else {
            this.bonus = bonus;
        }
    }

    // getters
    public String obterNome() {
        return this.nome;
    }

    public int obterBonus() {
        return this.bonus;
    }

    // descricao
    public String descricao() {
        return this.nome + " (+" + this.bonus + ")";
    }
}



// Classe principal
class Main {
    public static void main(String[] args) {

        // Criando personagem usando o construtor padrão
        Personagem personagem1 = new Personagem();

        // Criando personagem usando o construtor parametrizado
        Personagem personagem2 = new Personagem("Scrible", 80, 5);


        System.out.println("Personagem criado com construtor padrão:");
        System.out.println("Nome: " + personagem1.obterNome());
        System.out.println("Vida: " + personagem1.obterVida());
        System.out.println("Nível: " + personagem1.obterNivel());

        System.out.println("\nPersonagem criado com construtor parametrizado:");
        System.out.println("Nome: " + personagem2.obterNome());
        System.out.println("Vida: " + personagem2.obterVida());
        System.out.println("Nível: " + personagem2.obterNivel());


        System.out.println("\nTestando os ataques:");

        // Ataque padrão
        personagem1.atacar();

        // Ataque com dano definido
        personagem2.atacar(30);

        // testando item
        Item espada = new Item("Espada de Aço", 3);
        System.out.println(espada.descricao());

        Item espada_quebrada = new Item("Espada quebrada", -10);
        System.out.println(espada_quebrada.descricao());



    }
}
