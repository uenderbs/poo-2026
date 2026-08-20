// Projeto IF Quest
// Aula 2 - POO


// Classe com atributos e comportamentos de cada pesonagem
public class Personagem {
    String nome;
    int vida;
    int forca;


    void receberDano(int dano) {
        vida -= dano;
        System.out.println(nome + " sofreu " + dano + " de dano.");
    }

    boolean estaVivo() {
        return vida > 0;
    }

    String ficha() {
        return "Nome: " + nome + "\nVida: " + vida + "\nForça: " + forca;
    }

    void atacar(Personagem alvo) {
        System.out.println(nome + " ataca " + alvo.nome + " com " + forca + " de força.");
        alvo.receberDano(forca);   
    }
}

// Classe principal
class Main {
    public static void main(String[] args) {
        
        // Criando o herói
        Personagem heroi = new Personagem();
        heroi.nome = "Scribble";
        heroi.vida = 100;
        heroi.forca = 10;

        // Criando o chefe
        Personagem chefe = new Personagem();
        chefe.nome = "Dragão Azul de Olhos Vermelhos";
        chefe.vida = 200;
        chefe.forca = 20;

        // Ficha antes da batalha
        System.out.println("Ficha do Herói antes da Batalha:");
        System.out.println(heroi.ficha());
        System.out.println("------------------------------------\n");
        System.out.println("Ficha do Chefe antes da Batalha:");
        System.out.println(chefe.ficha());
        System.out.println("------------------------------------\n");

        System.out.println("---------- Início da Batalha ---------\n");


        // Simule uma batalha: cada personagem ataca o outro alternadamente até que um deles morra.
        while (heroi.estaVivo() && chefe.estaVivo()) {
            
            // Ataque do herói
            heroi.atacar(chefe);

            if (!chefe.estaVivo()) {
                System.out.println(chefe.nome + " está morto.");
                System.out.println(heroi.nome + " venceu a batalha!");
                break;
            }

            System.out.println();


            // Ataque do chefe
            chefe.atacar(heroi);

            if (!heroi.estaVivo()) {
                System.out.println(heroi.nome + " está morto.");
                System.out.println(chefe.nome + " venceu a batalha!");
                break;
            }
        }

        System.out.println();

        // Ficha depois da batalha
        System.out.println("Ficha do Herói depois da Batalha:");
        System.out.println(heroi.ficha());
        System.out.println("------------------------------------\n");
        System.out.println("Ficha do Chefe depois da Batalha:");
        System.out.println(chefe.ficha());
        System.out.println("------------------------------------\n");

        System.out.println("---------- Fim da Batalha ---------\n");
    
    }
}