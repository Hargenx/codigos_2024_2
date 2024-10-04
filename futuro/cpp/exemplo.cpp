#include <iostream>
#include <vector>
#include <cmath>
#include <SFML/Graphics.hpp> // Utilizada para visualização, pode ser substituída

// Estrutura para representar um círculo
struct Circle {
    sf::Vector2f position;  // Posição (x, y)
    float radius;           // Raio do círculo
    sf::Vector2f velocity;  // Velocidade (vx, vy)

    Circle(float x, float y, float r, float vx, float vy)
        : position(x, y), radius(r), velocity(vx, vy) {}
};

// Função para detectar colisão entre dois círculos
bool detectCollision(const Circle& c1, const Circle& c2) {
    float distX = c1.position.x - c2.position.x;
    float distY = c1.position.y - c2.position.y;
    float distance = std::sqrt(distX * distX + distY * distY);
    return distance < (c1.radius + c2.radius);
}

// Função para atualizar a posição de um círculo
void updatePosition(Circle& circle, float deltaTime) {
    circle.position.x += circle.velocity.x * deltaTime;
    circle.position.y += circle.velocity.y * deltaTime;
}

// Resolução de colisão simples: inverte a velocidade dos círculos em colisão
void resolveCollision(Circle& c1, Circle& c2) {
    std::swap(c1.velocity, c2.velocity);
}

int main() {
    sf::RenderWindow window(sf::VideoMode(800, 600), "Simulador de Colisão 2D");

    // Criando dois círculos em movimento
    Circle circle1(200, 300, 50, 200, 150);
    Circle circle2(600, 300, 50, -200, 150);

    sf::CircleShape shape1(circle1.radius);
    shape1.setFillColor(sf::Color::Green);
    shape1.setOrigin(circle1.radius, circle1.radius);

    sf::CircleShape shape2(circle2.radius);
    shape2.setFillColor(sf::Color::Blue);
    shape2.setOrigin(circle2.radius, circle2.radius);

    sf::Clock clock;

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        // Tempo decorrido
        float deltaTime = clock.restart().asSeconds();

        // Atualizar posições
        updatePosition(circle1, deltaTime);
        updatePosition(circle2, deltaTime);

        // Detectar e resolver colisões
        if (detectCollision(circle1, circle2)) {
            resolveCollision(circle1, circle2);
        }

        // Renderizar os círculos
        shape1.setPosition(circle1.position);
        shape2.setPosition(circle2.position);

        window.clear();
        window.draw(shape1);
        window.draw(shape2);
        window.display();
    }

    return 0;
}
