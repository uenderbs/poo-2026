// Projeto IF Quest
// Aula 3 - POO


// Classe com atributos e comportamentos de cada pesonagem
public class Personagem {
    private String nome;
    private int vida;
    private int nivel;

    public Personagem(String nome) {
        definirNome(nome);
        definirVida(100);
        definirNivel(1);
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


}



// Classe principal
class Main {
    public static void main(String[] args) {
        // Criando o personagem
        Personagem teste = new Personagem("Scrible");
        
        // Testando os métodos getter
        System.out.println("Nome: " + teste.obterNome());
        System.out.println("Vida: " + teste.obterVida());
        System.out.println("Nível: " + teste.obterNivel());

        System.out.println("\nAlterando os valores dos atributos...\n");
        
        // Testando os métodos setter
        teste.definirNome("Scrible 2");
        teste.definirVida(150);
        teste.definirNivel(0);

        // Testando os métodos getter novamente
        System.out.println("Nome: " + teste.obterNome());
        System.out.println("Vida: " + teste.obterVida());
        System.out.println("Nível: " + teste.obterNivel());

        // Testando a alteração de vida para um valor negativo
        teste.definirVida(-50);

        // Testando os métodos getter novamente após alteração
        System.out.println("\nApós tentar alterar a vida para um valor negativo:");
        System.out.println("Nome: " + teste.obterNome());
        System.out.println("Vida: " + teste.obterVida());
        System.out.println("Nível: " + teste.obterNivel());
    }
}