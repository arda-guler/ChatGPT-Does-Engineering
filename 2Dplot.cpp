#include <iostream>
#include <cmath>
#include <SDL2/SDL.h>

const int WIDTH = 640;
const int HEIGHT = 480;
const int MARGIN = 20;

int main()
{
    float data[] = {0.5, 0.2, 0.9, 0.1, 0.8, 0.3, 0.6, 0.4, 0.7}; // example data

    // Find max and min values
    float max_val = data[0];
    float min_val = data[0];
    for (int i = 1; i < 9; i++) {
        if (data[i] > max_val) {
            max_val = data[i];
        }
        if (data[i] < min_val) {
            min_val = data[i];
        }
    }

    // Initialize SDL
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        std::cerr << "Error initializing SDL: " << SDL_GetError() << std::endl;
        return 1;
    }

    // Create SDL window
    SDL_Window* window = SDL_CreateWindow("2D Plot", SDL_WINDOWPOS_CENTERED,
                                          SDL_WINDOWPOS_CENTERED, WIDTH,
                                          HEIGHT, SDL_WINDOW_SHOWN);
    if (window == nullptr) {
        std::cerr << "Error creating window: " << SDL_GetError() << std::endl;
        SDL_Quit();
        return 1;
    }

    // Create SDL renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (renderer == nullptr) {
        std::cerr << "Error creating renderer: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        SDL_Quit();
        return 1;
    }

    // Clear the screen
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
    SDL_RenderClear(renderer);

    // Draw x and y axis
    SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
    SDL_RenderDrawLine(renderer, MARGIN, MARGIN, MARGIN, HEIGHT - MARGIN);
    SDL_RenderDrawLine(renderer, MARGIN, HEIGHT - MARGIN, WIDTH - MARGIN, HEIGHT - MARGIN);

    // Draw data points
    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
    for (int i = 0; i < 8; i++) {
        int x = MARGIN + (i + 1) * ((WIDTH - 2 * MARGIN) / 9);
        int y = MARGIN + (data[i] - min_val) * (HEIGHT - 2 * MARGIN) / (max_val - min_val);
        SDL_RenderDrawPoint(renderer, x, HEIGHT - y - MARGIN);
    }

    // Update the screen
    SDL_RenderPresent(renderer);

    // Wait for user to close the window
    bool quit = false;
    SDL_Event event;
    while (!quit) {
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                quit = true;
            }
        }
    }

    // Clean up SDL
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
