### Informe del Laboratorio: Uso de Bandit para Análisis de Seguridad en Código Python

### Agenda del Laboratorio

1. **Introducción a Bandit**

   - Breve explicación de qué es Bandit y por qué es importante para la seguridad del código Python.
   - Ejemplo rápido de vulnerabilidades comunes que Bandit puede detectar (por ejemplo, uso inseguro de funciones, inyecciones, etc.).

2. **Configuración del Entorno Virtual**

   - Crear y activar un entorno virtual `venv`.
   - Instalar Bandit dentro del entorno virtual.

3. **Configuración Inicial y Ejemplos de Vulnerabilidades**

   - Crear un proyecto Python de ejemplo.
   - Incluir ejemplos de código con vulnerabilidades listadas en CWE.

4. **Uso Básico de Bandit**

   - Ejecutar Bandit en el proyecto.
   - Explicar la salida de Bandit: qué significan las diferentes secciones del reporte.
   - Mostrar cómo interpretar los resultados y priorizar las vulnerabilidades.

5. **Configuración Avanzada de Bandit**

   - Explicar cómo personalizar el análisis usando un archivo de configuración `.bandit`.
   - Ejemplo de configuración para ignorar ciertos tipos de vulnerabilidades.

### Detalles del Laboratorio

#### 1. Clonar el Repositorio y Preparar el Entorno

- **Clonar el Repositorio**

  ```sh
  git clone https://github.com/leoandy23/BanditLab.git
  cd BanditLab
  ```

- **Configuración del Entorno Virtual y Instalación de Dependencias**

  - Crear el entorno virtual:

    ```sh
    python -m venv venv
    ```

  - Activar el entorno virtual:

    - En Windows:
      ```sh
      venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

  - Instalar Bandit y requerimientos:
    ```sh
    pip install -r requirements.txt
    ```

#### 2. Configuración Inicial y Ejemplos de Vulnerabilidades

En esta sección se detallará cómo configurar el proyecto de ejemplo y qué vulnerabilidades se incluirán en los scripts.

- **Vulnerabilidades Incluidas:**

  - **Cross-site Scripting (XSS)**

    - **Descripción**: Permite a un atacante ejecutar scripts maliciosos en el navegador del usuario final.

  - **SQL Injection**

    - **Descripción**: Permite a un atacante manipular bases de datos al ejecutar comandos SQL no autorizados.

  - **OS Command Injection**

    - **Descripción**: Permite a un atacante ejecutar comandos del sistema operativo a través de entradas no validadas.

  - **Path Traversal**

    - **Descripción**: Permite a un atacante acceder a archivos fuera del directorio previsto mediante manipulación de rutas de archivo.

  - **Improper Input Validation**

    - **Descripción**: Permite la aceptación de datos no autorizados o maliciosos debido a una validación incorrecta.

  - **Missing Authentication for Critical Function**

    - **Descripción**: Permite a usuarios no autenticados ejecutar funciones críticas sin autenticación.

  - **Exposure of Sensitive Information to an Unauthorized Actor**

    - **Descripción**: Permite a un atacante acceder a información sensible, como registros de errores detallados, sin autorización.

  - **Improper Restriction of XML External Entity Reference (XXE)**

    - **Descripción**: Permite a un atacante leer archivos del sistema o realizar escaneos de puertos mediante entidades XML externas no seguras.

  - **Insertion of Sensitive Information into Log File**

    - **Descripción**: Permite la exposición de información sensible, como contraseñas o tokens de sesión, en archivos de registro.

  - **Use of a Broken or Risky Cryptographic Algorithm**
    - **Descripción**: Utiliza algoritmos criptográficos débiles o rotos que pueden comprometer la seguridad de los datos cifrados.

#### 3. Uso Básico de Bandit

- **Ejecutar Bandit en el Proyecto**

  Para ejecutar Bandit en todo el proyecto, utiliza el siguiente comando en tu terminal:

  ```sh
  bandit -r my_project/
  ```

  Donde `-r` indica que se debe realizar un análisis recursivo en el directorio `my_project/`.

- **Ejecutar Bandit en un fichero .py**
  Para ejecutar Bandit en un archivo específico, utiliza el siguiente comando en tu terminal:

  ```sh
  bandit mi_fichero.py
  ```

- **Interpretación de los Resultados de Bandit:**

  Después de ejecutar Bandit, recibirás un informe que incluye varios tipos de vulnerabilidades encontradas, junto con información detallada sobre cada una. Aquí hay algunos puntos clave para interpretar los resultados:

  - **ID de la Vulnerabilidad**: Cada vulnerabilidad detectada está identificada por un código único (por ejemplo, B101).
  - **Severidad**: Bandit clasifica la severidad de las vulnerabilidades como Alta, Media o Baja, basado en el potencial impacto de explotación.
  - **Descripción**: Una descripción breve de la vulnerabilidad encontrada y por qué es un problema de seguridad.
  - **Ubicación**: La ubicación exacta en el código donde se encontró la vulnerabilidad.
  - **Consejos de Mitigación**: Bandit a menudo proporciona consejos sobre cómo mitigar o corregir la vulnerabilidad detectada.

  - **Ejemplo de Resultado:**

    ```
    >> Issue: [B101:assert_used] Use of assert detected. The enclosed code will be removed when compiling to optimised byte code.
       Severity: Low   Confidence: High
       Location: ./example.py:10
       More Info: https://bandit.readthedocs.io/en/latest/plugins/b101_assert_used.html
       9 assert foo == bar
       10 assert baz == quux
       11 assert foobar
    ```

    En este ejemplo, Bandit detectó el uso de la declaración `assert` en el archivo `example.py` en la línea 10, lo cual es considerado una práctica de código riesgosa.

#### 4. Configuración Avanzada de Bandit

- **Personalizar el Análisis con `.bandit`**

  Para personalizar el análisis de Bandit según tus necesidades específicas, puedes crear un archivo `.bandit` en el directorio raíz de tu proyecto. Este archivo te permite configurar qué tipos de vulnerabilidades deseas incluir o excluir del análisis.

  - Ejemplo de configuración:

    ```yaml
        # FILE: .bandit
        [bandit]
        exclude = tests,path/to/file
        tests = B201,B301
        skips = B101,B601
    ```

  1. **`exclude`**:

  - **Descripción**: Este parámetro permite especificar qué archivos o directorios deben ser excluidos del análisis de Bandit.
  - **Ejemplo**: `exclude = tests,path/to/file` indica que los archivos en el directorio `tests` y el archivo o directorio `path/to/file` serán excluidos del análisis.

  2. **`tests`**:

  - **Descripción**: Aquí se especifica qué tipos de pruebas específicas de Bandit se deben ejecutar durante el análisis.
  - **Ejemplo**: `tests = B201,B301` indica que se deben ejecutar las pruebas correspondientes a las reglas `B201` y `B301`. Cada una de estas reglas representa un tipo específico de vulnerabilidad o problema de seguridad que Bandit puede detectar.

  3. **`skips`**:

  - **Descripción**: Este parámetro se utiliza para omitir (saltar) pruebas específicas de Bandit durante el análisis.
  - **Ejemplo**: `skips = B101,B601` indica que las pruebas correspondientes a las reglas `B101` y `B601` serán omitidas durante el análisis. Esto puede ser útil si ciertas reglas no son aplicables o relevantes para tu proyecto específico.

  Cada uno de estos parámetros te permite personalizar el análisis de Bandit según las necesidades y requisitos de seguridad de tu proyecto. Al configurar adecuadamente el archivo `.bandit`, puedes controlar qué aspectos del código se analizan, qué pruebas se ejecutan y qué pruebas se omiten, adaptándolo así a las particularidades de tu aplicación.

  - Guarda el archivo `.bandit` en el directorio raíz de tu proyecto y ejecuta Bandit nuevamente para observar cómo cambian los resultados según la configuración especificada.

**PARA MÁS INFORMACIÓN VISITAR LA DOCUMENTACIÓN OFICIAL DE [BANDIT](https://bandit.readthedocs.io/en/latest/index.html)**
