import {
  Component,
  type OnInit,
  type AfterViewInit,
  type OnDestroy,
  type ElementRef,
  ViewChild,
  Inject,
  PLATFORM_ID,
} from "@angular/core"
import { CommonModule, isPlatformBrowser } from "@angular/common"
import { RouterModule } from "@angular/router"

@Component({
  selector: "app-inicio",
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: "./inicio.component.html",
  styleUrls: ["./inicio.component.css"],
})
export class InicioComponent implements OnInit, AfterViewInit, OnDestroy {
  @ViewChild("magicButton") magicButton?: ElementRef

  title = "¡TU VOCACION ES NUESTRA MISION!"
  displayText = ""

  // Variables para controlar la animación
  private animationTimeoutId: any = null
  private particleTimeoutIds: any[] = []
  private isComponentActive = true
  private isBrowser: boolean;

  constructor(@Inject(PLATFORM_ID) private platformId: Object) {
    // Verificar si estamos en el navegador
    this.isBrowser = isPlatformBrowser(this.platformId)
  }

  ngOnInit(): void {
    
  }

  ngAfterViewInit(): void {
    // Solo ejecutar en el navegador
    if (this.isBrowser) {
      // Iniciar la animación de escritura con un pequeño retraso
      setTimeout(() => {
        if (this.isComponentActive) {
          this.startTypingAnimation()
        }
      }, 500)
    }
  }

  ngOnDestroy(): void {
    // Marcar el componente como inactivo
    this.isComponentActive = false

    // Solo ejecutar en el navegador
    if (this.isBrowser) {
      // Limpiar todos los timeouts pendientes
      if (this.animationTimeoutId !== null) {
        clearTimeout(this.animationTimeoutId)
      }

      // Limpiar timeouts de partículas
      this.particleTimeoutIds.forEach((id) => clearTimeout(id))
      this.particleTimeoutIds = []
    }
  }

  /**
   * Inicia la animación de escritura utilizando un enfoque no recursivo
   */
  startTypingAnimation(): void {
    if (!this.isBrowser) return

    let currentIndex = 0
    let isDeleting = false
    const typingSpeed = 150
    const pauseTime = 2000

    // Función para actualizar el texto mostrado
    const updateText = () => {
      if (!this.isComponentActive) return

      if (!isDeleting && currentIndex <= this.title.length) {
        // Escribiendo
        this.displayText = this.title.substring(0, currentIndex)
        currentIndex++

        if (currentIndex > this.title.length) {
          // Pausa antes de empezar a borrar
          isDeleting = true
          this.animationTimeoutId = setTimeout(updateText, pauseTime)
          return
        }
      } else if (isDeleting && currentIndex >= 0) {
        // Borrando
        this.displayText = this.title.substring(0, currentIndex)
        currentIndex--

        if (currentIndex === 0) {
          // Pausa antes de empezar a escribir de nuevo
          isDeleting = false
          this.animationTimeoutId = setTimeout(updateText, pauseTime)
          return
        }
      }

      // Programar la siguiente actualización
      this.animationTimeoutId = setTimeout(updateText, isDeleting ? typingSpeed / 2 : typingSpeed)
    }

    // Iniciar la animación
    updateText()
  }

  /**
   * Maneja el clic en el botón mágico
   */
  onButtonClick(): void {
    if (!this.isBrowser || !this.magicButton?.nativeElement) return

    const button = this.magicButton.nativeElement
    button.classList.add("animate-magic")

    // Crear partículas
    this.createParticles(button)

    // Eliminar la clase después de la animación
    setTimeout(() => {
      if (this.isComponentActive) {
        button.classList.remove("animate-magic")
      }
    }, 700)
  }

  /**
   * Crea partículas para el efecto mágico
   */
  createParticles(button: HTMLElement): void {
    if (!this.isBrowser || !this.isComponentActive) return

    const buttonRect = button.getBoundingClientRect()
    const particleCount = 20
    const particles: HTMLElement[] = []
    const document = this.isBrowser ? window.document : null

    if (!document) return

    // Crear todas las partículas de una vez
    for (let i = 0; i < particleCount; i++) {
      const particle = document.createElement("div")
      particle.classList.add("magic-particle")

      // Posición inicial (centro del botón)
      const x = buttonRect.left + buttonRect.width / 2
      const y = buttonRect.top + buttonRect.height / 2

      // Ángulo aleatorio y distancia
      const angle = Math.random() * Math.PI * 2
      const distance = Math.random() * 100 + 50

      // Posición final
      const destX = x + Math.cos(angle) * distance
      const destY = y + Math.sin(angle) * distance

      // Tamaño aleatorio
      const size = Math.random() * 8 + 4

      // Color aleatorio (azules y morados)
      const colors = ["#4F46E5", "#6366F1", "#8B5CF6", "#A78BFA", "#C4B5FD"]
      const color = colors[Math.floor(Math.random() * colors.length)]

      // Aplicar estilos
      particle.style.position = "fixed"
      particle.style.width = `${size}px`
      particle.style.height = `${size}px`
      particle.style.backgroundColor = color
      particle.style.borderRadius = "50%"
      particle.style.left = `${x}px`
      particle.style.top = `${y}px`
      particle.style.pointerEvents = "none"
      particle.style.zIndex = "1000"

      document.body.appendChild(particle)
      particles.push(particle)

      // Animación
      const duration = Math.random() * 1000 + 500

      // Usar la API de animación web para mejor rendimiento
      const animation = particle.animate(
        [
          { transform: `translate(0, 0) scale(0)`, opacity: 1 },
          { transform: `translate(${destX - x}px, ${destY - y}px) scale(1)`, opacity: 0 },
        ],
        {
          duration,
          easing: "cubic-bezier(0.1, 0.8, 0.2, 1)",
        },
      )

      // Eliminar partícula después de la animación
      const timeoutId = setTimeout(() => {
        if (document.body.contains(particle)) {
          document.body.removeChild(particle)
        }

        // Eliminar el ID del timeout de la lista
        const index = this.particleTimeoutIds.indexOf(timeoutId)
        if (index !== -1) {
          this.particleTimeoutIds.splice(index, 1)
        }
      }, duration)

      // Guardar el ID del timeout para limpieza
      this.particleTimeoutIds.push(timeoutId)
    }
  }
}
