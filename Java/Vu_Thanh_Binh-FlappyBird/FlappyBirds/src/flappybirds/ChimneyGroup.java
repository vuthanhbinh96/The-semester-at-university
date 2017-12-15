/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package flappybirds;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Random;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;
import pkg2dgamesframework.QueueList;

/**
 *
 * @author BinhBietBoi
 */
public class ChimneyGroup {
    private QueueList<Chimney> chimneys;
    
    private BufferedImage chimneyImage,chimneyImage2;
    
    public static int SIZE = 6;
    
    private int topChimney = -330;
    private int botChimney = 220;
    
    public Chimney getChimney(int i){
        return chimneys.get(i);
    }
    
    public int getRandomY(){
        Random random = new Random();
        int a;
        a = random.nextInt(25);
        return a*10;
    }
    
    public ChimneyGroup(){
        
        try {
            chimneyImage = ImageIO.read(new File ("Assets/chimney.png"));
            chimneyImage2 = ImageIO.read(new File ("Assets/chimney_.png"));
        } catch (IOException ex) {
            Logger.getLogger(FlappyBirds.class.getName()).log(Level.SEVERE, null, ex);
        }
        
        chimneys = new QueueList<>();
        
        Chimney cn;
        
        for(int i = 0; i<SIZE/2;i++){
            
            int detalY = getRandomY();
            
            cn = new Chimney(830+i*300,botChimney+detalY,74,400);
            chimneys.push(cn);
            
            cn = new Chimney(830+i*300,topChimney+detalY,74,400);
            chimneys.push(cn);
             
        }
    }
    
    public void resetGame(){
        chimneys = new QueueList<>();
        
        Chimney cn;
        
        for(int i = 0; i<SIZE/2;i++){
            
            int detalY = getRandomY();
            
            cn = new Chimney(830+i*300,botChimney+detalY,74,400);
            chimneys.push(cn);
            
            cn = new Chimney(830+i*300,topChimney+detalY,74,400);
            chimneys.push(cn);
             
        }
    }

    public void paint(Graphics2D g2){
        for(int i=0;i<6;i++){
            if(i%2==0)
                g2.drawImage(chimneyImage,(int)chimneys.get(i).getPosX(),(int)chimneys.get(i).getPosY(),null);
            else
                g2.drawImage(chimneyImage2,(int)chimneys.get(i).getPosX(),(int)chimneys.get(i).getPosY(),null);
        }
    }
    
    public void update(){
        for(int i = 0;i<SIZE ; i++){
            chimneys.get(i).update();
        }
        
        if(chimneys.get(0).getPosX()<-74){
            
            int detalY = getRandomY();
            
            Chimney cn;
            cn = chimneys.pop();
            cn.setPosX(chimneys.get(4).getPosX() + 300);
            cn.setPosY(botChimney+detalY);
            cn.setIsBehindBird(false);
            chimneys.push(cn);
            
            cn = chimneys.pop();
            cn.setPosX(chimneys.get(4).getPosX());   
            cn.setPosY(topChimney+detalY);
            cn.setIsBehindBird(false);
            chimneys.push(cn);
        }
        
    }
}    
