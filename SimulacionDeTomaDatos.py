% Simulación de recolección de datos de humedad y temperatura por un dron en clima tropical

% Definir el tiempo de simulación
tiempo_simulacion = 3600; % Duración de la simulación en segundos (1 hora)

% Crear un vector de tiempo con intervalos de 1 segundo
tiempo = 0:1:tiempo_simulacion;

% Inicializar vectores para datos simulados de humedad y temperatura
datos_humedad = zeros(size(tiempo));
datos_temperatura = zeros(size(tiempo));

% Parámetros de procesos estocásticos para humedad y temperatura
media_humedad = 70; % Valor medio de humedad en porcentaje
desviacion_humedad = 5; % Desviación estándar de humedad
media_temperatura = 30; % Valor medio de temperatura en grados Celsius
desviacion_temperatura = 3; % Desviación estándar de temperatura

% Simulación de recolección de datos y vuelo del dron
% Inicializamos las coordenadas del dron
posicion_x = zeros(size(tiempo));
posicion_y = zeros(size(tiempo));
posicion_z = zeros(size(tiempo));

% Definimos el punto de inicio del dron
posicion_x(1) = 0;
posicion_y(1) = 0;
posicion_z(1) = 0;

% Intervalo de toma de datos (cada 1 minuto)
intervalo_toma_datos = 60; % 1 minuto en segundos
ultima_toma_datos = 0;

% Vectores para almacenar datos de temperatura y tiempo de toma de datos
temperaturas_tomadas = [];
tiempos_toma_datos = [];

% Simulación del vuelo en un marco tropical ficticio
for t = 2:length(tiempo)
    % Simulación de cambios aleatorios en humedad y temperatura como procesos estocásticos
    datos_humedad(t) = normrnd(media_humedad, desviacion_humedad);
    datos_temperatura(t) = normrnd(media_temperatura, desviacion_temperatura);
    
    % Simulación de movimiento del dron en un marco tridimensional ficticio
    % Aquí puedes ajustar la lógica de vuelo según tus necesidades.
    % En este ejemplo, el dron se mueve aleatoriamente en x, y, y z.
    posicion_x(t) = posicion_x(t-1) + rand() * 2 - 1; % Movimiento aleatorio en x
    posicion_y(t) = posicion_y(t-1) + rand() * 2 - 1; % Movimiento aleatorio en y
    posicion_z(t) = posicion_z(t-1) + rand() * 2 - 1; % Movimiento aleatorio en z
    
    % Toma de datos de temperatura cada 1 minuto
    if tiempo(t) - ultima_toma_datos >= intervalo_toma_datos
        temperaturas_tomadas = [temperaturas_tomadas, datos_temperatura(t)];
        tiempos_toma_datos = [tiempos_toma_datos, tiempo(t)];
        ultima_toma_datos = tiempo(t);
    end
end

% Visualización del vuelo del dron en un marco tridimensional ficticio
figure;
plot3(posicion_x, posicion_y, posicion_z, 'b');
title('Vuelo del Dron en un Marco Tropical');
xlabel('Posición X');
ylabel('Posición Y');
zlabel('Posición Z');
grid on;

% Visualización de datos de humedad y temperatura
figure;
subplot(2, 1, 1);
plot(tiempo, datos_humedad);
title('Datos de Humedad (Proceso Estocástico)');
xlabel('Tiempo (s)');
ylabel('Humedad (%)');

subplot(2, 1, 2);
plot(tiempo, datos_temperatura);
title('Datos de Temperatura (Proceso Estocástico)');
xlabel('Tiempo (s)');
ylabel('Temperatura (°C)');

% Análisis de variables de Atterberg (ejemplo)
% Puedes calcular las variables de Atterberg utilizando los datos de humedad
% y temperatura simulados. Asegúrate de tener una función adecuada para esto.
% Por ejemplo, supongamos que tienes una función 'calcularVariablesAtterberg'
% que toma los datos de humedad y temperatura como entrada y calcula las
% variables de Atterberg. Puedes llamar a esta función aquí.

VariablesAtterberg = calcularVariablesAtterberg(datos_humedad, datos_temperatura);

% Visualización de variables de Atterberg
figure;
subplot(3, 1, 1);
plot(tiempo, VariablesAtterberg.indice_plasticidad);
title('Índice de Plasticidad');
xlabel('Tiempo (s)');
ylabel('Índice de Plasticidad');

subplot(3, 1, 2);
plot(tiempo, VariablesAtterberg.limite_liquido);
title('Límite Líquido');
xlabel('Tiempo (s)');
ylabel('Límite Líquido');

subplot(3, 1, 3);
plot(tiempo, VariablesAtterberg.limite_plastico);
title('Límite Plástico');
xlabel('Tiempo (s)');
ylabel('Límite Plástico');

% Gráfico de regresión lineal para los datos de temperatura
figure;
scatter(tiempos_toma_datos, temperaturas_tomadas, 'b', 'filled');
hold on;
p = polyfit(tiempos_toma_datos, temperaturas_tomadas, 1);
temperaturas_predichas = polyval(p, tiempos_toma_datos);
plot(tiempos_toma_datos, temperaturas_predichas, 'r', 'LineWidth', 2);
title('Regresión Lineal de Temperatura');
xlabel('Tiempo (s)');
ylabel('Temperatura (°C)');
legend('Datos de Temperatura', 'Regresión Lineal');


% Gráfico de regresión de árbol de decisión para los datos de temperatura
figure;
scatter(tiempos_toma_datos, temperaturas_tomadas, 'b', 'filled');
hold on;

% Crear y entrenar el modelo de regresión de árbol de decisión
mdl = fitrtree(tiempos_toma_datos', temperaturas_tomadas');
temperaturas_predichas = predict(mdl, tiempos_toma_datos');
plot(tiempos_toma_datos, temperaturas_predichas, 'r', 'LineWidth', 2);
title('Regresión de Árbol de Decisión para Temperatura');
xlabel('Tiempo (s)');
ylabel('Temperatura (°C)');
legend('Datos de Temperatura', 'Regresión de Árbol de Decisión');




% Cálculo de correlaciones entre variables de Atterberg y otras variables
correlacion_humedad_indice_plasticidad = corr(datos_humedad', VariablesAtterberg.indice_plasticidad');
correlacion_temperatura_indice_plasticidad = corr(datos_temperatura', VariablesAtterberg.indice_plasticidad');
correlacion_posicion_x_indice_plasticidad = corr(posicion_x', VariablesAtterberg.indice_plasticidad');
correlacion_posicion_y_indice_plasticidad = corr(posicion_y', VariablesAtterberg.indice_plasticidad');
correlacion_posicion_z_indice_plasticidad = corr(posicion_z', VariablesAtterberg.indice_plasticidad');

% Visualización de las correlaciones
fprintf('Correlación Humedad vs. Índice de Plasticidad: %.2f\n', correlacion_humedad_indice_plasticidad);
fprintf('Correlación Temperatura vs. Índice de Plasticidad: %.2f\n', correlacion_temperatura_indice_plasticidad);
fprintf('Correlación Posición X vs. Índice de Plasticidad: %.2f\n', correlacion_posicion_x_indice_plasticidad);
fprintf('Correlación Posición Y vs. Índice de Plasticidad: %.2f\n', correlacion_posicion_y_indice_plasticidad);
fprintf('Correlación Posición Z vs. Índice de Plasticidad: %.2f\n', correlacion_posicion_z_indice_plasticidad);

% Crear un modelo de regresión para predecir el límite líquido en función de las demás variables
X = [datos_humedad', datos_temperatura', posicion_x', posicion_y', posicion_z'];
y = VariablesAtterberg.limite_liquido';

mdl = fitlm(X, y);

% Supongamos que tienes datos simulados de condiciones de vuelo y humedad
% Crear datos simulados de condiciones de vuelo y humedad
condiciones_vuelo = rand(size(tiempo)); % Datos simulados de condiciones de vuelo
humedad_simulada = rand(size(tiempo)); % Datos simulados de humedad

% Calcular la correlación entre todas las variables
correlacion_indice_plasticidad = corr([VariablesAtterberg.indice_plasticidad', temperaturas_tomadas', condiciones_vuelo', humedad_simulada']);
correlacion_limite_liquido = corr([VariablesAtterberg.limite_liquido', temperaturas_tomadas', condiciones_vuelo', humedad_simulada']);
correlacion_limite_plastico = corr([VariablesAtterberg.limite_plastico', temperaturas_tomadas', condiciones_vuelo', humedad_simulada']);

% Crear un gráfico de matriz de correlación
figure;
correlation_matrix = [correlacion_indice_plasticidad; correlacion_limite_liquido; correlacion_limite_plastico];
imagesc(correlation_matrix);
colorbar;
colormap('jet');
xticklabels({'Índice de Plasticidad', 'Temperatura', 'Condiciones de Vuelo', 'Humedad'});
yticklabels({'Índice de Plasticidad', 'Límite Líquido', 'Límite Plástico'});
title('Matriz de Correlación Múltiple');


% Visualización de resultados del modelo
fprintf('Coeficientes del modelo:\n');
disp(mdl.Coefficients.Estimate);

% Función para calcular variables de Atterberg
function VariablesAtterberg = calcularVariablesAtterberg(datos_humedad, datos_temperatura)
    % Inicializar variables de Atterberg
    indice_plasticidad = zeros(size(datos_humedad));
    limite_liquido = zeros(size(datos_humedad));
    limite_plastico = zeros(size(datos_humedad));
    
    % Simulación de cálculos de las variables de Atterberg
    for t = 1:length(datos_humedad)
        % Simulación de cálculos (en este caso, valores aleatorios)
        % Reemplaza esto con cálculos reales basados en los datos de humedad
        % y temperatura si los tienes disponibles.
        
        indice_plasticidad(t) = rand() * 20; % Valor aleatorio entre 0 y 20
        limite_liquido(t) = 20 + rand() * 10; % Valor aleatorio entre 20 y 30
        limite_plastico(t) = limite_liquido(t) - indice_plasticidad(t); % Límite plástico
        
        % Puedes realizar cálculos más realistas utilizando tus datos y ecuaciones.
    end
    
    % Almacenar los resultados en una estructura
    VariablesAtterberg.indice_plasticidad = indice_plasticidad;
    VariablesAtterberg.limite_liquido = limite_liquido;
    VariablesAtterberg.limite_plastico = limite_plastico;
end
